# FASE 10 — IA GENERATIVA 2D

> **Posição na trilha:** Primeira metade da Fase 9 original — split justificado pelo volume e pela diferença de carreira.
> **Nível:** Estado da Arte (Avançado/Pesquisa)
> **Tempo estimado:** 2–3 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 06 (Transformers + CLIP) e Fase 04 (PyTorch arquiteto)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### PyTorch Nível Arquiteto (Fases 04 e 05)

* Backpropagation customizado (saber onde o gradiente flui)
* Estruturas encoder-decoder (U-Net da Fase 08)
* Fluxo completo de treino, debug e avaliação

### Transformers e Atenção (Fase 06)

* Self-attention e cross-attention implementados
* Como texto guia imagem via cross-attention
* CLIP: embeddings de texto e imagem no mesmo espaço

### Probabilidade e Estatística (Fase 01)

* **CRÍTICO:** Distribuições normais, amostragem (sampling)
* Valor esperado, variância
* KL Divergence (Kullback-Leibler): entender a fórmula e a intuição

### 🚨 Aviso Importante

> Você **não vai treinar Stable Diffusion no seu PC**. Você vai:
> - Implementar versões miniatura para entender as arquiteturas
> - Fazer fine-tuning (LoRA) em modelos open-source
> - Usar HuggingFace Diffusers para inferência e customização
>
> Quem tenta treinar modelos fundacionais em casa perde semanas sem resultado.

---

## 🔹 BLOCO 1 — AUTOENCODERS CLÁSSICOS (PONTO DE PARTIDA)

### O que é um Autoencoder

```
Entrada (x)
    ↓ Encoder
Vetor Latente (z) — comprimido
    ↓ Decoder
Reconstrução (x̂) ≈ x
```

**Loss:** `L = ||x - x̂||²` (reconstrução pixel a pixel)

```python
class Autoencoder(nn.Module):
    def __init__(self, latent_dim=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 256), nn.ReLU(),
            nn.Linear(256, latent_dim)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256), nn.ReLU(),
            nn.Linear(256, 28*28), nn.Sigmoid(),
            nn.Unflatten(1, (1, 28, 28))
        )
    
    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)
```

### O Problema do Autoencoder para Geração

**Espaço latente "esburacado":**
* Pontos de treinamento mapeados para regiões isoladas
* Interpolação entre dois pontos gera imagens sem sentido
* Não serve para **gerar** imagens novas, só para **comprimir/reconstruir**

---

## 🔹 BLOCO 2 — VAE (VARIATIONAL AUTOENCODER)

> A grande sacada: em vez de mapear para um ponto fixo no espaço latente, mapear para uma **distribuição de probabilidade**.

### A Ideia Central

```
Autoencoder clássico:
  x → encoder → z (ponto fixo) → decoder → x̂

VAE:
  x → encoder → μ, σ (parâmetros de distribuição) → Sample z ~ N(μ, σ²) → decoder → x̂
```

### Reparameterization Trick (CRÍTICO)

**O problema:** `z ~ N(μ, σ²)` é uma operação estocástica — o gradiente não pode fluir através de "sortear um valor aleatório".

**A solução:** Separar o ruído do parâmetro aprendível:

```
z = μ + σ * ε,  onde ε ~ N(0, 1)
```

Agora o gradiente flui por `μ` e `σ` (parâmetros da rede) — `ε` é só ruído externo.

### Loss Function do VAE (Dois Termos)

```
L_VAE = L_reconstrução + β * L_KL

L_reconstrução = ||x - x̂||²  (ou BCE para pixels binários)

L_KL = -0.5 * Σ (1 + log(σ²) - μ² - σ²)
         Força distribuição latente → Normal padrão N(0, 1)
```

**Intuição do L_KL:** Evita que o encoder colapse para pontos isolados. Força o espaço latente a ser "organizado" — permite interpolação e geração.

### Implementação Completa

```python
class VAE(nn.Module):
    def __init__(self, latent_dim=64):
        super().__init__()
        
        # Encoder → μ e log_var (não σ — mais estável numericamente)
        self.encoder_shared = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU()
        )
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_log_var = nn.Linear(256, latent_dim)
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256), nn.ReLU(),
            nn.Linear(256, 512), nn.ReLU(),
            nn.Linear(512, 28*28), nn.Sigmoid(),
            nn.Unflatten(1, (1, 28, 28))
        )
    
    def encode(self, x):
        h = self.encoder_shared(x)
        return self.fc_mu(h), self.fc_log_var(h)
    
    def reparametrize(self, mu, log_var):
        # Reparameterization trick
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)  # N(0,1), mesmo shape que std
        return mu + std * eps
    
    def forward(self, x):
        mu, log_var = self.encode(x)
        z = self.reparametrize(mu, log_var)
        return self.decoder(z), mu, log_var

def vae_loss(reconstrucao, x, mu, log_var, beta=1.0):
    # Reconstrução (BCE)
    bce = F.binary_cross_entropy(reconstrucao, x, reduction='sum')
    # KL Divergence
    kl = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
    return bce + beta * kl
```

### Geração e Interpolação

```python
# Gerar imagem nova a partir de ruído
with torch.no_grad():
    z_novo = torch.randn(1, latent_dim)
    img_gerada = vae.decoder(z_novo)

# Interpolar entre duas imagens
z1 = vae.encode(img1)[0]  # μ de img1
z2 = vae.encode(img2)[0]  # μ de img2

for alpha in np.linspace(0, 1, 8):
    z_interp = (1 - alpha) * z1 + alpha * z2
    img_interp = vae.decoder(z_interp)
```

### 🚧 Exercício Obrigatório

* Implementar VAE para MNIST ou CelebA
* Gerar grade de imagens a partir de ruído aleatório
* Implementar interpolação entre duas imagens reais
* Visualizar o espaço latente 2D com t-SNE

---

## 🔹 BLOCO 3 — GANs (GENERATIVE ADVERSARIAL NETWORKS)

> O treino adversarial é um dos conceitos mais inteligentes e mais frustrantes em ML. A teoria é elegante. A prática é uma guerra de hiperparâmetros.

### A Dinâmica do Jogo (Minimax)

```
Generator (G): Noise z → Imagem Falsa
Discriminator (D): Imagem → Probabilidade [0=falsa, 1=real]

Objetivo do G: Enganar D (fazer D classificar falsa como 1)
Objetivo do D: Não ser enganado (classificar real=1, falsa=0)

Equilíbrio de Nash: G gera imagens tão boas que D fica em 50% (não consegue distinguir)
```

### Losses Formais

```python
# D quer maximizar: log D(x_real) + log(1 - D(G(z)))
# G quer minimizar: log(1 - D(G(z))) → equiv. maximizar log D(G(z))

criterio = nn.BCELoss()
reais = torch.ones(batch, 1)   # Labels: real = 1
falsos = torch.zeros(batch, 1) # Labels: falso = 0

# Treinar Discriminador
pred_real = D(imgs_reais)
pred_falso = D(G(z).detach())  # detach: não propagar para G aqui
loss_D = criterio(pred_real, reais) + criterio(pred_falso, falsos)

# Treinar Generator
pred_falso_g = D(G(z))
loss_G = criterio(pred_falso_g, reais)  # G quer que D classifique como real
```

### DCGAN (Deep Convolutional GAN)

```python
class Generator(nn.Module):
    def __init__(self, z_dim=100, img_channels=3, features=64):
        super().__init__()
        self.gen = nn.Sequential(
            # z_dim → 4×4
            self._block(z_dim, features*16, 4, 1, 0),        # 4×4
            self._block(features*16, features*8, 4, 2, 1),   # 8×8
            self._block(features*8, features*4, 4, 2, 1),    # 16×16
            self._block(features*4, features*2, 4, 2, 1),    # 32×32
            nn.ConvTranspose2d(features*2, img_channels, 4, 2, 1),  # 64×64
            nn.Tanh()  # [-1, 1] → normalização padrão de GAN
        )
    
    def _block(self, in_ch, out_ch, k, s, p):
        return nn.Sequential(
            nn.ConvTranspose2d(in_ch, out_ch, k, s, p, bias=False),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(True)
        )
    
    def forward(self, z):
        return self.gen(z.view(-1, z.shape[1], 1, 1))
```

### Problemas Críticos (O Inferno de Engenharia)

**Mode Collapse**
* G descobre 1 imagem que engana D e só gera ela repetidamente
* Sintoma: grade de imagens geradas todas iguais
* Soluções: Wasserstein Loss (WGAN), Label Smoothing, Unrolled GAN

**Vanishing Gradient**
* D fica tão bom que D(G(z)) → 0 → gradient de G desaparece
* G não aprende mais nada

**Instabilidade de Treino**
* Pequena mudança em lr → D domina G ou vice-versa → ciclo de colapso

### Boas Práticas para Estabilidade

```python
# 1. Usar LeakyReLU no Discriminador (não ReLU puro)
nn.LeakyReLU(0.2)

# 2. Label Smoothing (real = 0.9, não 1.0)
reais_suaves = 0.9 * torch.ones(batch, 1)

# 3. BatchNorm (exceto na 1ª camada do D e última do G)

# 4. Adam com lr=2e-4, betas=(0.5, 0.999) — padrão DCGAN

# 5. Treinar D mais vezes que G por step (ratio 1:2 ou 1:5)
for _ in range(n_critic):
    # Treinar D
    ...
# Treinar G uma vez
```

### 🚧 Projeto Obrigatório

* Treinar DCGAN para gerar imagens de animes, pokémons ou fashion-MNIST
* Monitorar loss de G e D ao longo do treino
* Documentar se ocorreu mode collapse e como você lidou

---

## 🔹 BLOCO 4 — MODELOS DE DIFUSÃO (CORAÇÃO DO ESTADO DA ARTE)

> DDPM (2020) + Latent Diffusion (2022) = Stable Diffusion. Entender isso é entender o que está por trás de Midjourney, DALL-E e Sora.

### A Física da Difusão

**Forward Process (Destruição controlada):**
```
x₀ (imagem limpa)
    ↓ adicionar ruído gaussiano gradualmente
x₁ (levemente ruidosa)
    ↓
x₂
    ↓ ...
x_T (ruído branco — não há mais informação da imagem)
```

```python
# Cronograma de ruído (noise schedule)
betas = torch.linspace(0.0001, 0.02, T)  # T=1000 timesteps
alphas = 1 - betas
alphas_cumprod = torch.cumprod(alphas, dim=0)

# Amostrar x_t diretamente a partir de x_0 (sem precisar de todos os passos)
def q_sample(x0, t, noise=None):
    if noise is None:
        noise = torch.randn_like(x0)
    sqrt_alpha = alphas_cumprod[t].sqrt().view(-1, 1, 1, 1)
    sqrt_one_minus = (1 - alphas_cumprod[t]).sqrt().view(-1, 1, 1, 1)
    return sqrt_alpha * x0 + sqrt_one_minus * noise
```

**Reverse Process (O modelo aprende a desfazer):**

A rede neural **não aprende a imagem diretamente**. Ela aprende a **prever o ruído** que foi adicionado:

```
U-Net(x_t, t) → ε_pred (ruído estimado)
Loss = ||ε - ε_pred||²   (onde ε é o ruído real que foi adicionado)
```

### Implementação Simplificada (Toy DDPM)

```python
class ToyDDPM(nn.Module):
    """U-Net simplificada para dados de baixa resolução."""
    def __init__(self, channels=1, time_emb_dim=32):
        super().__init__()
        # Embedding do timestep (o modelo precisa saber em qual step está)
        self.time_mlp = nn.Sequential(
            SinusoidalPositionEmbs(time_emb_dim),
            nn.Linear(time_emb_dim, time_emb_dim*4),
            nn.GELU(),
        )
        # Arquitetura U-Net modificada (aceita timestep)
        # ... (simplificado para legibilidade)
    
    def forward(self, x, t):
        """
        x: imagem ruidosa (batch, channels, H, W)
        t: timestep (batch,) — qual passo da difusão
        Retorna: ruído estimado ε_pred
        """
        t_emb = self.time_mlp(t)
        # ... processar x condicionado em t_emb
        return ruido_estimado

# Loop de treino
for batch in loader:
    x0 = batch  # Imagens limpas
    t = torch.randint(0, T, (batch_size,))  # Timestep aleatório
    noise = torch.randn_like(x0)
    x_t = q_sample(x0, t, noise)  # Imagem ruidosa no timestep t
    
    predicted_noise = model(x_t, t)
    loss = F.mse_loss(predicted_noise, noise)  # Comparar ruído predito com real
    
    optimizer.zero_grad(); loss.backward(); optimizer.step()
```

### Sampling (Geração)

```python
@torch.no_grad()
def p_sample_loop(model, shape):
    """Gerar imagem partindo de ruído puro."""
    img = torch.randn(*shape)  # x_T: ruído puro
    
    for t in reversed(range(0, T)):
        t_batch = torch.full((shape[0],), t)
        predicted_noise = model(img, t_batch)
        
        # Fórmula de DDPM para x_{t-1} dado x_t e ε_pred
        alpha = alphas[t]
        alpha_bar = alphas_cumprod[t]
        beta = betas[t]
        
        img = (1 / alpha.sqrt()) * (img - beta / (1 - alpha_bar).sqrt() * predicted_noise)
        
        if t > 0:  # Adicionar ruído exceto no último passo
            img += beta.sqrt() * torch.randn_like(img)
    
    return img.clamp(-1, 1)
```

### Latent Diffusion (O que torna tudo rápido)

**Problema:** Rodar difusão em imagem 512×512 é computacionalmente insuportável (1000 passos × 3 × 512 × 512).

**Solução em 2 etapas:**

```
1. VAE Encoder:   x (512×512×3) → z (64×64×4)     ← 48x menor!
2. Difusão:       Rodar DDPM no espaço latente z    ← muito mais rápido
3. VAE Decoder:   z̃ (64×64×4) → x̂ (512×512×3)    ← reconstruir
```

**Cross-Attention para guiar com texto:**
```
CLIP Text Encoder → embeddings de texto
    ↓
Injetar em cada camada da U-Net via cross-attention
    ↓
U-Net agora sabe "para onde" denoisar
```

### Fine-Tuning com LoRA

```python
# LoRA: treinar só matrizes de baixo rank — 99% menor que treinar tudo
from diffusers import StableDiffusionPipeline
from peft import get_peft_model, LoraConfig

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Aplicar LoRA só nas camadas de atenção
lora_config = LoraConfig(
    r=4,                    # Rank (baixo = menos parâmetros)
    lora_alpha=32,
    target_modules=["to_k", "to_q", "to_v", "to_out.0"],
    lora_dropout=0.1
)
pipe.unet = get_peft_model(pipe.unet, lora_config)
```

### 🚧 Mini-projeto Obrigatório

* Implementar Toy DDPM para dados 2D simples ou MNIST
* Visualizar: processo de destruição (x₀ → x_T) e geração (x_T → x₀)
* Bonus: Fine-tune Stable Diffusion com LoRA em estilo artístico

---

## 🔹 BLOCO 5 — MANIPULAÇÃO NO ESPAÇO LATENTE

> Com VAE e Diffusion treinados, o espaço latente tem estrutura semântica. Você pode navegar nele.

### Interpolação Latente com VAEs

```python
# Transição suave entre dois rostos
z1 = encoder(rosto_triste)
z2 = encoder(rosto_feliz)

imagens_transicao = []
for alpha in np.linspace(0, 1, 10):
    z_interp = (1 - alpha) * z1 + alpha * z2
    img = decoder(z_interp)
    imagens_transicao.append(img)
```

### Aritmética Latente (como word2vec de imagens)

```python
# "Homem com óculos" - "Homem" + "Mulher" = "Mulher com óculos"
z_homem_oculos = encoder(img_homem_oculos)
z_homem = encoder(img_homem)
z_mulher = encoder(img_mulher)

z_resultado = z_homem_oculos - z_homem + z_mulher
img_resultado = decoder(z_resultado)
```

### 🚧 Projeto Obrigatório

* Treinar VAE em dataset de faces (CelebA subset)
* Encontrar vetores de atributo: `v_sorriso`, `v_oculos`, `v_barba`
* Aplicar e remover atributos matematicamente

---

## 🧪 PROJETOS OBRIGATÓRIOS DE PORTFÓLIO

### 1️⃣ Seu Próprio Mini "Midjourney"

* Implementar DDPM do zero
* Treinar em dataset temático pequeno (sprites de jogos, ícones, emojis, fashion)
* Interface: digitar descrição → gerar imagem (LoRA em SD ou toy model)
* **Meta:** Demonstrar geração de imagens novas coerentes com o dataset

### 2️⃣ Sistema de Interpolação Visual

* Treinar VAE ou usar embeddings CLIP
* Interface: enviar 2 imagens → gerar 8 frames de transição entre elas
* Demonstrar aritmética latente: A - B + C = D

### 3️⃣ Fine-Tuning com LoRA

* Escolher estilo artístico (pintura a óleo, anime, pixel art)
* Fine-tunar Stable Diffusion com LoRA em 20-50 imagens do estilo
* Comparar: prompts com e sem o estilo treinado

### 4️⃣ Análise Comparativa

* Comparar 3 abordagens para o mesmo dataset:
  * Autoencoder → reconstuição pura
  * VAE → geração com interpolação
  * DCGAN → geração adversarial
* Documentar qualidade visual, modo de colapso, dificuldade de treino

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Autoencoders clássicos (implementar + treinar)
2. Problema do espaço latente "esburacado"
3. VAE: reparameterization trick
4. Loss VAE (reconstrução + KL)
5. Interpolação e aritmética latente com VAE
6. GAN: dinâmica do jogo (teoria)
7. DCGAN (implementar do zero)
8. Problemas: mode collapse, gradients vanishing
9. Técnicas de estabilização
10. DDPM: forward process (adicionar ruído)
11. DDPM: reverse process (prever ruído)
12. Toy DDPM (implementar e treinar)
13. Latent Diffusion (conceito + uso HuggingFace)
14. Fine-tuning com LoRA
15. **Projetos de portfólio**

---

## 🚨 ERROS FATAIS NESTA FASE

* Tentar treinar Stable Diffusion do zero no PC — impossível sem cluster de GPU
* Usar WebUIs (ComfyUI, A1111) sem entender o código por baixo
* Pular implementação manual do VAE e DDPM
* Ignorar mode collapse — debugar é parte do aprendizado
* Não visualizar o espaço latente (o principal insight desta fase é a estrutura semântica)

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 11 se:

* [ ] Explica Reparameterization Trick no quadro branco sem consultar nada
* [ ] Implementa e treina VAE com interpolação funcional
* [ ] Treina DCGAN sem mode collapse imediato (estabiliza o treino)
* [ ] Implementa DDPM toy (forward + reverse) e gera imagens
* [ ] Entende como cross-attention conecta texto a pixels em SD
* [ ] Fine-tuna Stable Diffusion com LoRA em estilo próprio
