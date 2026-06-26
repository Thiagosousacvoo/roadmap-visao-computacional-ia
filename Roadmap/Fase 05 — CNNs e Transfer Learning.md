# FASE 05 — REDES NEURAIS CONVOLUCIONAIS (CNN)

> **Posição na trilha:** Aqui a IA começa a "ver" imagens de verdade — automaticamente aprende quais features extrair.
> **Nível:** Avançado
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fases 03 (convolução manual) e 04 (PyTorch sólido) completas

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Deep Learning (Fase 04 sólida)

* Entender forward pass e backpropagation
* Saber o que é tensor e como funciona `nn.Module`
* Treinar modelo simples no PyTorch **sem copiar tutorial**

👉 Se você ainda copia código → NÃO avance

### Imagem como Matriz (Fase 03)

* RGB = `(H, W, C)` → em PyTorch: `(C, H, W)`
* Manipular imagem com NumPy/OpenCV
* Entender o que é convolução manualmente

### PyTorch Prático

* Dataset + DataLoader funcionando
* Loop de treino completo
* Loss + Optimizer

---

## 🔹 BLOCO 1 — CONVOLUÇÃO (NÍVEL ENGENHEIRO)

> A diferença entre um usuário de CNN e um engenheiro de CNN é: o engenheiro consegue prever o shape da saída sem rodar o código.

### Anatomia da Camada Convolucional

**Parâmetros da `nn.Conv2d`:**

```python
nn.Conv2d(
    in_channels=3,     # Canais de entrada (3 para RGB)
    out_channels=32,   # Número de filtros (= feature maps na saída)
    kernel_size=3,     # Tamanho do kernel (3 = 3×3)
    stride=1,          # Passo do kernel
    padding=1,         # Borda adicionada para manter tamanho
    bias=True
)
```

### Fórmula de Shape da Saída (CRÍTICO)

```
H_out = floor((H_in + 2*padding - kernel_size) / stride) + 1
W_out = floor((W_in + 2*padding - kernel_size) / stride) + 1
```

**Exemplos práticos:**

| Entrada | kernel | stride | padding | Saída |
|---|---|---|---|---|
| (1, 3, 224, 224) | 3×3 | 1 | 1 | (1, 32, 224, 224) |
| (1, 3, 224, 224) | 3×3 | 2 | 1 | (1, 64, 112, 112) |
| (1, 3, 224, 224) | 7×7 | 2 | 3 | (1, 64, 112, 112) |

### Stride

* `stride=1` (padrão): kernel se move 1 pixel por vez
* `stride=2`: reduz dimensão por 2 (alternativa ao pooling)

### Padding

* `padding=0` ("valid"): saída menor que entrada
* `padding=kernel_size//2` ("same"): saída mantém dimensão

### 🎯 Domínio

* Conseguir prever shape da saída **sem rodar código**

### 🚧 Exercício obrigatório

1. Calcular shapes manualmente para 5 configs diferentes
2. Verificar com `x = torch.randn(1, 3, 224, 224); print(conv(x).shape)`

---

## 🔹 BLOCO 2 — FEATURE MAPS

> Cada filtro em uma camada Conv aprende a detectar um padrão específico. Com 32 filtros, você tem 32 "perspectivas" diferentes da imagem.

### O que são Feature Maps

```
Entrada: (1, 3, 224, 224)     ← 1 imagem RGB
              ↓ Conv2d(3→32, k=3)
Saída:   (1, 32, 224, 224)    ← 32 feature maps
```

Cada um dos 32 feature maps responde a um padrão diferente:
* Feature map 0: responde a bordas verticais
* Feature map 1: responde a bordas horizontais  
* Feature map 7: responde a cantos
* Feature map 20: responde a texturas específicas

### Visualizar Feature Maps

```python
# Extrair saída de uma camada
activation = {}
def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()
    return hook

model.conv1.register_forward_hook(get_activation('conv1'))
output = model(img_tensor)

# Plotar feature maps
fig, axes = plt.subplots(4, 8, figsize=(16, 8))
for i, ax in enumerate(axes.flat):
    if i < activation['conv1'].shape[1]:
        ax.imshow(activation['conv1'][0, i].numpy(), cmap='viridis')
    ax.axis('off')
```

---

## 🔹 BLOCO 3 — ARQUITETURA CNN COMPLETA

### Pipeline

```
Imagem (C, H, W)
    ↓
[Conv2d → BatchNorm → ReLU → MaxPool] × N    ← Blocos de extração
    ↓
Flatten ou AdaptiveAvgPool2d
    ↓
[Linear → ReLU → Dropout] × M                ← Classificador
    ↓
Linear → Softmax/Sigmoid                      ← Saída
```

### Pooling

**MaxPooling**
```python
nn.MaxPool2d(kernel_size=2, stride=2)
# Reduz H e W pela metade, mantém canais
# Pega o valor máximo em cada janela 2×2
```

**AveragePooling**
```python
nn.AvgPool2d(2, 2)
```

**Global Average Pooling (GAP)**
```python
nn.AdaptiveAvgPool2d(1)  # → shape (batch, channels, 1, 1)
# Alternativa ao Flatten — melhor para transfer learning
```

### Flatten

```python
nn.Flatten()  # (batch, C, H, W) → (batch, C*H*W)
# Ou: x.view(x.size(0), -1)
```

### 🎯 Domínio

* Entender o fluxo completo da imagem até a saída
* Saber calcular o shape em cada etapa

### 🚧 Exercício

* Desenhar no papel a arquitetura antes de codar
* Incluir shapes em cada camada

---

## 🔹 BLOCO 4 — PRIMEIRA CNN: MNIST → CIFAR-10

### CNN para MNIST

```python
class CNNMnist(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),  # (1,28,28)→(32,28,28)
            nn.ReLU(),
            nn.MaxPool2d(2, 2),              # (32,28,28)→(32,14,14)
            nn.Conv2d(32, 64, 3, padding=1), # (32,14,14)→(64,14,14)
            nn.ReLU(),
            nn.MaxPool2d(2, 2),              # (64,14,14)→(64,7,7)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),                    # (64,7,7)→(3136)
            nn.Linear(64*7*7, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 10)
        )
    
    def forward(self, x):
        return self.classifier(self.features(x))
```

**Meta:** > 99% accuracy em MNIST

### Evolução para CIFAR-10

**Diferenças:**
* 3 canais RGB (não 1)
* Imagens 32×32
* 10 classes mais difíceis (aviões, carros, pássaros...)
* Requer rede mais profunda

**Meta:** > 85% accuracy em CIFAR-10 (sem transfer learning)

---

## 🔹 BLOCO 5 — DATA AUGMENTATION

> Mais dados = melhor generalização. Data augmentation é a forma de "multiplicar" seu dataset artificialmente.

### Transformações com torchvision

```python
from torchvision import transforms

# Para TREINO (com augmentation):
transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=10),
    transforms.RandomCrop(32, padding=4),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Para VALIDAÇÃO/TESTE (sem augmentation!):
transform_val = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])
```

> ⚠️ **Nunca** aplicar augmentation em validação/teste — apenas no treino

### Normalização (por que esses valores?)

Os valores `[0.485, 0.456, 0.406]` são a média e desvio padrão calculados sobre o **ImageNet** (dataset de 1.2M imagens). Modelos pré-treinados esperam exatamente essa normalização.

### 🚧 Exercício

* Treinar CIFAR-10 com e sem augmentation
* Comparar curvas de loss e accuracy final (esperado: ~5-10% de ganho)

---

## 🔹 BLOCO 6 — ARQUITETURAS CLÁSSICAS (ENTENDER A EVOLUÇÃO)

> Não é para implementar todas do zero. É para entender por que cada uma foi criada e o problema que resolve.

### LeNet-5 (1998)

* Primeira CNN bem-sucedida
* 2 camadas conv + 3 FC
* Base conceitual de tudo

### AlexNet (2012)

* Venceu ImageNet com margem absurda
* Trouxe: ReLU, dropout, GPU training
* Prova que CNN profunda funciona

### VGG (2014)

* Kernels sempre 3×3 (descoberta: profundidade > kernel grande)
* VGG16 e VGG19 ainda usados em transfer learning

### ResNet (2015) — CRÍTICO

**O problema:** Redes muito profundas sofrem de "degradação" — adicionar mais camadas piora o resultado. Por quê? Gradiente desaparece nas primeiras camadas.

**A solução — Skip Connection:**

```python
# Bloco residual simples
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)
    
    def forward(self, x):
        residual = x                          # ← Guardar entrada
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out = out + residual                  # ← Somar com entrada original
        return F.relu(out)
```

**Por que funciona:** O gradiente tem um "caminho direto" pelas skip connections — não precisa atravessar as camadas convolucionais (que podem sumir o gradiente).

### EfficientNet (2019)

* Escala largura, profundidade e resolução de forma balanceada
* Atualmente um dos mais usados em produção real

---

## 🔹 BLOCO 7 — TRANSFER LEARNING (MUNDO REAL)

> 90% dos projetos reais de visão não treinam CNN do zero. Usam transfer learning.

### Por que funciona?

Redes treinadas no ImageNet aprenderam features universais:
* Camadas iniciais: detectam bordas, cores, texturas
* Camadas intermediárias: detectam partes (olhos, rodas)
* Camadas finais: detectam objetos completos

Para um novo problema, você aproveita tudo isso e só treina as últimas camadas.

### Estratégias

**1. Feature Extraction (camadas congeladas)**
```python
modelo = torchvision.models.resnet50(pretrained=True)

# Congelar todas as camadas
for param in modelo.parameters():
    param.requires_grad = False

# Substituir apenas a última camada
num_classes = 5
modelo.fc = nn.Linear(modelo.fc.in_features, num_classes)
# Só `modelo.fc` tem requires_grad=True
```

**2. Fine-Tuning (camadas descongeladas gradualmente)**
```python
# Descongelar últimas N camadas
for param in modelo.layer4.parameters():
    param.requires_grad = True

# Usar lr menor para não destruir features pré-treinadas
otimizador = torch.optim.Adam([
    {'params': modelo.layer4.parameters(), 'lr': 1e-4},
    {'params': modelo.fc.parameters(), 'lr': 1e-3}
])
```

**Quando usar qual:**
* Dataset pequeno + similar ao ImageNet → Feature extraction
* Dataset médio → Fine-tuning das últimas camadas
* Dataset grande → Fine-tuning de tudo (ou treinar do zero)

### 🚧 Projetos

1. **Gatos vs Cachorros:** ResNet18 com feature extraction — deve atingir > 95% com dataset de 1000 imagens
2. **Dataset próprio:** Criar dataset com suas próprias fotos (mínimo 3 classes, 100 imagens por classe)

---

## 🔹 BLOCO 8 — VISION TRANSFORMERS (ViT) — INTRODUÇÃO

> ViT não usa convolução. Divide a imagem em patches (pedaços) e aplica o mecanismo de atenção — o mesmo de modelos de linguagem.

### Por que estudar aqui?

Na **Fase 06 (NLP & Transformers)** você vai aprender o mecanismo de atenção em profundidade. Este bloco é uma **introdução conceitual** — você vai entender completamente na próxima fase.

### Conceito

```
Imagem (224×224)
    ↓
Dividir em patches de 16×16 → 196 patches
    ↓
Cada patch → vetor de embedding (como token de texto)
    ↓
Position encoding (manter informação espacial)
    ↓
Self-Attention entre todos os patches
    ↓
Classificação
```

### CNN vs ViT

| | CNN | ViT |
|---|---|---|
| Receptive field | Local (vizinhança imediata) | Global (todos os patches) |
| Inductive bias | Sim (localidade, equivariância) | Mínimo |
| Dado necessário | Menos dados | Muito mais dados |
| Performance | Excelente em datasets médios | Estado da arte em datasets grandes |

### Uso prático hoje

```python
import timm

modelo = timm.create_model('vit_base_patch16_224', pretrained=True, num_classes=10)
```

### 🎯 Domínio

* Entender a diferença conceitual CNN vs ViT
* Saber quando um é melhor que o outro
* **Implementação completa na Fase 06**

---

## 🧪 PROJETOS OBRIGATÓRIOS

### 1️⃣ CNN do zero (MNIST)

* Arquitetura sua (não copiar)
* > 99% accuracy

### 2️⃣ CNN CIFAR-10

* 3 canais RGB
* Comparar: com e sem data augmentation
* > 85% accuracy

### 3️⃣ Transfer Learning com ResNet

* Congelar camadas + trocar head
* Dataset próprio (suas fotos)
* > 90% accuracy com > 3 classes

### 4️⃣ Análise de erros

* Visualizar os 20 exemplos que o modelo mais errou
* Formular hipótese sobre por que errou
* Aplicar melhoria baseada na hipótese

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Fórmula de shape de convolução (praticar manualmente)
2. `nn.Conv2d` no PyTorch + visualizar saída
3. MaxPooling, Average Pooling, GAP
4. Arquitectura CNN completa (papel → código)
5. MNIST com CNN
6. CIFAR-10 (aumentar complexidade)
7. Data augmentation (comparar com e sem)
8. Arquiteturas clássicas (LeNet → ResNet, entender evolução)
9. Skip connections (ResNet — implementar bloco residual)
10. Transfer learning — feature extraction
11. Transfer learning — fine-tuning
12. Dataset próprio
13. ViT (conceito + uso com `timm`)
14. **Análise de erros (projeto 4)**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Não entender shape → erro número 1 em CNN
* Copiar arquitetura pronta sem entender cada camada
* Ignorar overfitting (treino alto, val baixo)
* Não usar data augmentation
* Pular transfer learning (irrealista no mercado — ninguém treina ResNet do zero)
* Aplicar normalização errada ao usar modelo pré-treinado

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 06 se:

* [ ] Constrói CNN do zero e explica cada camada e shape
* [ ] Ajusta modelo sozinho baseado nas curvas de loss
* [ ] Usa transfer learning corretamente (normalização certa, lr diferenciado)
* [ ] Resolve problema real com imagens próprias (> 90% accuracy)
* [ ] Entende a diferença conceitual entre CNN e ViT
* [ ] Analisa erros do modelo e aplica melhoria justificada


---
