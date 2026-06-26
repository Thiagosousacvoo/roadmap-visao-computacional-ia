# FASE 10 — IA GENERATIVA 2D

> **Posição na trilha:** Primeira metade da Fase 9 original — split justificado pelo volume e pela diferença de carreira.
> **Nível:** Estado da Arte (Avançado/Pesquisa)
> **Tempo estimado:** 2–3 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 06 (Transformers + CLIP) e Fase 04 (PyTorch arquiteto)

> ⚠️ 🆕 **Nota de validação temporal (esta revisão):** esta é, junto da Fase 11, a fase que mais envelhece rápido em todo o roadmap. Os fundamentos (VAE, GAN, DDPM, cross-attention) são estáveis e continuam válidos — mas as ferramentas/modelos específicos citados (versão do Stable Diffusion, bibliotecas de LoRA, modelos VLM citados no Bloco 6) merecem uma checagem rápida de "isso ainda é o padrão atual?" antes de investir tempo profundo.

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

## 🔹 BLOCO 6 — SELF-SUPERVISED LEARNING (SSL) 🆕 (Adição desta revisão)

> Este bloco é conceitual, não pesado em implementação — o objetivo é você conhecer a ferramenta e saber quando puxá-la, não implementar um pipeline de pré-treino completo do zero.

### O Problema que SSL Resolve

Ao longo do roadmap você usou repetidamente o padrão: "pegar modelo pré-treinado no ImageNet (Fase 05) → fine-tunar para o seu problema". Isso funciona muito bem quando seu domínio é parecido com fotos naturais do ImageNet. **Mas e quando seu domínio é muito diferente** (imagens médicas, industriais, satélite, microscopia) **e você não tem volume suficiente de dados rotulados** nesse domínio específico?

```
Resposta clássica:  "Anote mais dados" (caro, lento)
Resposta com SSL:   "Pré-treine um encoder usando os dados NÃO rotulados
                      que você já tem em abundância do seu próprio domínio
                      — e SÓ DEPOIS faça fine-tuning supervisionado com
                      o pouco de dado rotulado que você tem"
```

Isso conecta diretamente com a Fase 05, Bloco 7 (Transfer Learning): SSL é a evolução de "ImageNet pretrained" para "pretrained no SEU domínio, sem precisar de rótulo".

### Contrastive Learning (SimCLR — Intuição)

```
Ideia central: pegar a MESMA imagem, aplicar duas augmentations diferentes
(crop, color jitter, flip) → o modelo deve aprender que essas duas versões
são "a mesma coisa" (embeddings próximos), e diferentes de outras imagens
do batch (embeddings distantes)

Imagem X
   ├─→ Augmentation A → Encoder → embedding_A  ┐
   └─→ Augmentation B → Encoder → embedding_B  ┘→ aproximar (loss contrastiva)

Imagem Y (outra do batch) → embedding_Y → afastar de embedding_A e embedding_B
```

```python
# Esqueleto conceitual (não é para implementar peso por peso — é para entender o fluxo)
import torch.nn.functional as F

def nt_xent_loss(z_a, z_b, temperatura=0.5):
    """Loss contrastiva (NT-Xent) usada no SimCLR — simplificada para 1 par."""
    z_a, z_b = F.normalize(z_a, dim=-1), F.normalize(z_b, dim=-1)
    similaridade = (z_a @ z_b.T) / temperatura
    labels = torch.arange(z_a.size(0))  # cada item é seu próprio "par positivo"
    return F.cross_entropy(similaridade, labels)
```

### Self-Distillation (DINO — Intuição, Sem Rótulo Nenhum)

```
Duas cópias da mesma rede (uma "professor", atualizada lentamente; uma
"aluno", atualizada normalmente). Ambas veem versões diferentes (crops)
da mesma imagem. O aluno aprende a prever a saída do professor.

Resultado surpreendente: sem NUNCA ver um rótulo, o encoder aprende
features que separam objetos e até captura noção de "partes" do objeto
(efeito observado nos mapas de atenção do DINO em ViTs).
```

### Quando Vale Usar SSL no Seu Projeto

| Cenário | Vale usar SSL? |
|---|---|
| Domínio parecido com fotos naturais (objetos do dia a dia) | Não — ImageNet pretrained (Fase 05) já resolve bem |
| Domínio muito específico (imagens médicas, industriais, microscopia) + muitas imagens SEM rótulo disponíveis | Sim — pré-treine um encoder com SSL no seu próprio domínio antes do fine-tuning supervisionado |
| Pouquíssimos dados, rotulados ou não | SSL não cria dado do nada — ajuda mas não substitui volume mínimo |

### 🎯 Domínio

* Entender a diferença entre "pretrained genérico" (ImageNet) e "pretrained no seu domínio via SSL"
* Saber identificar quando SSL é a ferramenta certa (muito dado não-rotulado, domínio fora do ImageNet) vs. quando é desperdício de esforço (domínio já bem coberto por modelos genéricos)

### 🚧 Exercício (conceitual + prático leve)

* Usar um encoder pré-treinado via SSL já disponível (ex: DINOv2 via `torch.hub`) e comparar os embeddings extraídos dele com os de um ResNet ImageNet comum, no seu dataset de algum projeto anterior (Fase 05 ou 07)
* Não é necessário treinar SSL do zero — o objetivo é saber usar e interpretar, não reimplementar o paper

---

## 🔹 BLOCO 7 — VISION-LANGUAGE MODELS (VLMs) MODERNOS 🆕 (Adição desta revisão)

> A Fase 06 ensinou CLIP corretamente — embeddings de imagem e texto no mesmo espaço, ótimo para similaridade e classificação zero-shot. Mas CLIP **não gera texto** — ele só mede similaridade. Este bloco cobre a categoria de modelo que veio depois: VLMs completos, que combinam um encoder visual com um modelo de linguagem para **descrever, responder perguntas sobre, e raciocinar sobre** uma imagem.

### CLIP vs. VLM Completo — A Diferença Que Importa

```
CLIP:
  Imagem → embedding (512d)  ┐
  Texto  → embedding (512d)  ┘→ similaridade (um número)
  Não gera texto novo. Só compara.

VLM completo (estilo LLaVA / GPT-4V):
  Imagem → Vision Encoder → projeta no espaço do LLM
  Prompt: "O que está acontecendo nesta imagem?"
  Saída: texto gerado livremente, descrevendo/raciocinando sobre a imagem
```

### Arquitetura Típica (Visão de Engenheiro)

```
Imagem → Vision Encoder (geralmente um ViT, às vezes o próprio CLIP) 
              ↓
         Camada de projeção (adapta a dimensão do embedding visual
         para o espaço de embedding do LLM)
              ↓
         Embeddings visuais são inseridos na sequência de tokens,
         junto com o prompt de texto
              ↓
         LLM (decoder, igual ao que você viu na Fase 06) gera a
         resposta token a token, agora "vendo" a imagem
```

### Uso Prático (Captioning e VQA)

```python
from transformers import pipeline

# Captioning: descrever a imagem automaticamente
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
resultado = captioner("foto.jpg")
print(resultado[0]["generated_text"])

# VQA (Visual Question Answering): perguntar sobre a imagem
vqa = pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")
resposta = vqa(image="foto.jpg", question="Quantas pessoas estão na imagem?")
print(resposta)
```

```python
# Para um VLM mais completo e conversacional (estilo LLaVA), via API de modelo
# multimodal aberto — a interface exata varia por modelo/provedor, mas o padrão é:
mensagens = [
    {"role": "user", "content": [
        {"type": "image", "image": "foto_linha_producao.jpg"},
        {"type": "text", "text": "Existe algum produto com defeito visível nesta imagem? Descreva."}
    ]}
]
resposta = modelo_vlm.generate(mensagens)
```

### Caso de Uso Real Conectado ao Resto do Roadmap

> Um uso de produção genuinamente útil: usar um VLM como **QA automático de dataset**. Depois de treinar seu detector (Fase 07) ou segmentador (Fase 08), você pode rodar um VLM em lote sobre as imagens onde o modelo teve baixa confiança (conectando com Active Learning, Fase 09 Bloco 7) e pedir para ele descrever a cena — isso ajuda a entender rapidamente *por que* o modelo está com dúvida, sem precisar olhar imagem por imagem manualmente.

### Quando Usar VLM vs. CLIP vs. Detector/Segmentador Especializado

| Necessidade | Ferramenta certa |
|---|---|
| "Essas duas imagens são semanticamente parecidas?" | CLIP (embeddings + similaridade) |
| "Buscar imagens por descrição em texto" | CLIP (Fase 06, projeto de busca visual) |
| "Descrever o que está acontecendo na cena, em linguagem livre" | VLM completo (este bloco) |
| "Onde exatamente está o objeto X, com bounding box ou máscara" | Detector (Fase 07) / Segmentador (Fase 08) — VLM não dá localização precisa de forma confiável |
| "Responder pergunta aberta sobre a imagem" | VLM completo (VQA) |

### 🎯 Domínio

* Saber articular a diferença entre CLIP (similaridade) e VLM completo (geração de texto sobre imagem) — isso é frequentemente confundido e é uma pergunta natural de entrevista
* Usar um VLM pronto para captioning/VQA sem precisar treinar nada do zero

### 🚧 Exercício

* Rodar captioning automático em 20 imagens de algum dataset de projeto anterior (Fase 07 ou 08)
* Comparar as legendas geradas com as classes/anotações que você já tinha — identificar onde o VLM "viu" algo que sua anotação original não capturava

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
15. 🆕 Self-Supervised Learning: SimCLR e DINO (conceito + uso de encoder pré-treinado)
16. 🆕 VLMs modernos: captioning e VQA na prática
17. **Projetos de portfólio**

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
* [ ] 🆕 Explica quando SSL vale a pena vs. transfer learning tradicional
* [ ] 🆕 Usa um VLM moderno para captioning/VQA e articula a diferença com CLIP


---
