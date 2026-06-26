# FASE 08 — SEGMENTAÇÃO

> **Posição na trilha:** Evolução de bounding box para previsão pixel a pixel — cada pixel recebe uma classe.
> **Nível:** Avançado
> **Tempo estimado:** 2–3 semanas (dedicação intensiva de 8–12h/dia) — 🛠️ ajustado nesta revisão (era 1-2 semanas) para acomodar o Bloco 9 (SAM/SAM2)
> **Pré-requisito:** Fases 05 (CNN sólida) e 07 (Object Detection)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### CNN (Fase 05 sólida)

* Convolução, feature maps, pooling
* Controle de shape (CRÍTICO — shapes são mais complexos aqui)

### Object Detection (Fase 07)

* Bounding box, IoU
* Dataset e anotação
* Treino com YOLO

👉 Segmentação é evolução direta de detecção

### PyTorch

* Dataset customizado, DataLoader
* Loop de treino completo

---

## 🔹 BLOCO 1 — TIPOS DE SEGMENTAÇÃO

### Segmentação Semântica

* Cada pixel → classe global (pessoa, carro, fundo)
* Todos os pixels da mesma classe = mesma "cor"
* Não distingue instâncias separadas (duas pessoas = mesmo rótulo)

```
Entrada: (3, H, W) RGB
Saída:   (num_classes, H, W) — mapa de probabilidades por classe
         ou (H, W) — mapa de classes (argmax)
```

### Segmentação de Instâncias

* Cada pixel → instância específica de objeto
* Pessoa 1 ≠ Pessoa 2 mesmo sendo da mesma classe
* Combina detecção + segmentação

### Segmentação Panóptica

* Unifica semântica + instâncias
* "Stuff" (fundo, céu, grama) → semântico
* "Things" (pessoas, carros) → instâncias
* Estado da arte completo

---

## 🔹 BLOCO 2 — REPRESENTAÇÃO DE MÁSCARA (CRÍTICO)

### Máscara Binária

```python
# 0 → fundo, 1 → objeto
mascara = np.zeros((H, W), dtype=np.uint8)
mascara[100:200, 150:300] = 1  # Região do objeto
```

### Máscara Multi-classe

```python
# Cada pixel = inteiro representando a classe
mascara = np.zeros((H, W), dtype=np.uint8)
# 0 = fundo, 1 = pessoa, 2 = carro, 3 = bicicleta...
```

### One-Hot Encoding

```python
# Para loss: (num_classes, H, W) — cada canal = mapa binário de uma classe
def to_one_hot(mascara, num_classes):
    one_hot = np.zeros((num_classes, *mascara.shape))
    for c in range(num_classes):
        one_hot[c] = (mascara == c).astype(float)
    return one_hot
```

### Estrutura do Dataset de Segmentação

```
dataset/
├── images/
│   ├── train/
│   │   ├── img001.jpg
│   │   └── img002.jpg
│   └── val/
│       └── img003.jpg
└── masks/
    ├── train/
    │   ├── img001.png    ← MESMO nome, extensão .png
    │   └── img002.png    ← Máscara: pixels com valor da classe
    └── val/
        └── img003.png
```

**Regra crítica:** Imagem e máscara devem ter:
* Mesmo nome de arquivo
* Mesma dimensão `(H, W)`
* A máscara é aplicada pixel-a-pixel

### Carregar e Visualizar

```python
import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread("images/train/img001.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mascara = cv2.imread("masks/train/img001.png", cv2.IMREAD_GRAYSCALE)

# Overlay da máscara na imagem
def overlay_mascara(img, mascara, alpha=0.5):
    colormap = plt.cm.get_cmap('tab10', mascara.max() + 1)
    mascara_cor = (colormap(mascara)[:, :, :3] * 255).astype(np.uint8)
    return cv2.addWeighted(img, 1-alpha, mascara_cor, alpha, 0)

resultado = overlay_mascara(img, mascara)
```

### Dataset PyTorch Customizado

```python
class SegmentationDataset(Dataset):
    def __init__(self, img_dir, mask_dir, transform=None, mask_transform=None):
        self.img_paths = sorted(glob(f"{img_dir}/*.jpg"))
        self.mask_paths = sorted(glob(f"{mask_dir}/*.png"))
        self.transform = transform
        self.mask_transform = mask_transform
    
    def __len__(self):
        return len(self.img_paths)
    
    def __getitem__(self, idx):
        img = Image.open(self.img_paths[idx]).convert("RGB")
        mask = Image.open(self.mask_paths[idx])
        
        # CRÍTICO: mesma transformação geométrica em imagem E máscara
        if self.transform:
            img = self.transform(img)
        if self.mask_transform:
            mask = self.mask_transform(mask)
        
        return img, mask
```

> ⚠️ **Armadilha:** Data augmentation geométrico (flip, rotação) deve ser aplicado **igualmente** à imagem e à máscara. Nunca separadamente.

### 🚧 Exercício obrigatório

1. Carregar par (imagem, máscara)
2. Exibir lado a lado
3. Sobrepor máscara colorida na imagem
4. Verificar alinhamento pixel a pixel

---

## 🔹 BLOCO 3 — FUNÇÕES DE PERDA (CRÍTICO)

### Binary Cross-Entropy (BCE)

```python
# Para segmentação binária (1 classe)
criterio = nn.BCEWithLogitsLoss()
loss = criterio(predicao, mascara.float())
```

### Dice Loss

```python
def dice_loss(pred, target, smooth=1.0):
    pred = torch.sigmoid(pred)
    pred = pred.view(-1)
    target = target.view(-1)
    
    intersecao = (pred * target).sum()
    dice = (2. * intersecao + smooth) / (pred.sum() + target.sum() + smooth)
    return 1 - dice
```

* Mede sobreposição entre predição e máscara real
* Especialmente útil quando objeto ocupa pequena fração da imagem

### Focal Loss

```python
def focal_loss(pred, target, alpha=0.25, gamma=2):
    bce = F.binary_cross_entropy_with_logits(pred, target, reduction='none')
    pt = torch.exp(-bce)
    focal = alpha * (1 - pt) ** gamma * bce
    return focal.mean()
```

* Foca em exemplos difíceis (pixels na borda, casos raros)
* Reduz peso de exemplos fáceis que dominam o treino

### Combinação Prática

```python
def combined_loss(pred, target, bce_weight=0.5, dice_weight=0.5):
    bce = F.binary_cross_entropy_with_logits(pred, target)
    dice = dice_loss(pred, target)
    return bce_weight * bce + dice_weight * dice
```

### 🎯 Domínio

| Cenário | Loss recomendada |
|---|---|
| Segmentação binária, classes balanceadas | BCE |
| Segmentação binária, objeto pequeno | Dice ou BCE + Dice |
| Múltiplas classes, desbalanceado | Focal Loss |
| Produção geral | BCE + Dice (combinação) |

---

## 🔹 BLOCO 4 — U-NET (ARQUITETURA BASE DA INDÚSTRIA)

> U-Net é usada em praticamente todos os projetos sérios de segmentação: médica, satélite, industrial.

### Arquitetura

```
Entrada (3, 256, 256)
│
├─ [Conv → BN → ReLU] × 2 → MaxPool    (encoder nível 1: 64ch, 128×128)
├─ [Conv → BN → ReLU] × 2 → MaxPool    (encoder nível 2: 128ch, 64×64)
├─ [Conv → BN → ReLU] × 2 → MaxPool    (encoder nível 3: 256ch, 32×32)
├─ [Conv → BN → ReLU] × 2 → MaxPool    (encoder nível 4: 512ch, 16×16)
│
└─ BOTTLENECK (1024ch, 8×8)
│
├─ UpConv + Concatenar com encoder 4   → (512ch, 16×16)
├─ UpConv + Concatenar com encoder 3   → (256ch, 32×32)
├─ UpConv + Concatenar com encoder 2   → (128ch, 64×64)
├─ UpConv + Concatenar com encoder 1   → (64ch, 128×128)
│
└─ Conv 1×1 → Saída (num_classes, 256, 256)
```

### Implementação PyTorch

```python
class DoubleConv(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )
    def forward(self, x):
        return self.conv(x)

class UNet(nn.Module):
    def __init__(self, in_channels=3, num_classes=1):
        super().__init__()
        
        # Encoder
        self.e1 = DoubleConv(in_channels, 64)
        self.e2 = DoubleConv(64, 128)
        self.e3 = DoubleConv(128, 256)
        self.e4 = DoubleConv(256, 512)
        self.bottleneck = DoubleConv(512, 1024)
        self.pool = nn.MaxPool2d(2, 2)
        
        # Decoder
        self.up4 = nn.ConvTranspose2d(1024, 512, 2, stride=2)
        self.d4 = DoubleConv(1024, 512)  # 512 (up) + 512 (skip) = 1024
        self.up3 = nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.d3 = DoubleConv(512, 256)
        self.up2 = nn.ConvTranspose2d(256, 128, 2, stride=2)
        self.d2 = DoubleConv(256, 128)
        self.up1 = nn.ConvTranspose2d(128, 64, 2, stride=2)
        self.d1 = DoubleConv(128, 64)
        
        self.final = nn.Conv2d(64, num_classes, 1)
    
    def forward(self, x):
        # Encoder
        s1 = self.e1(x)
        s2 = self.e2(self.pool(s1))
        s3 = self.e3(self.pool(s2))
        s4 = self.e4(self.pool(s3))
        b = self.bottleneck(self.pool(s4))
        
        # Decoder com skip connections
        d4 = self.d4(torch.cat([self.up4(b), s4], dim=1))
        d3 = self.d3(torch.cat([self.up3(d4), s3], dim=1))
        d2 = self.d2(torch.cat([self.up2(d3), s2], dim=1))
        d1 = self.d1(torch.cat([self.up1(d2), s1], dim=1))
        
        return self.final(d1)
```

### Por que Skip Connections?

* O encoder comprime informação (perde detalhes espaciais)
* O decoder precisa reconstruir a máscara na resolução original
* **Skip connections passam detalhes finos direto do encoder para o decoder**
* Sem skip connections: máscara reconstruída fica "borrada"

---

## 🔹 BLOCO 5 — VISUALIZAÇÃO E DEBUG (OBRIGATÓRIO)

```python
def plotar_predicao(img, mascara_real, mascara_pred, threshold=0.5):
    """Plotar imagem, máscara real e máscara predita lado a lado."""
    pred_bin = (torch.sigmoid(mascara_pred) > threshold).float()
    
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    axes[0].imshow(img.permute(1,2,0).numpy())
    axes[0].set_title("Imagem Original")
    axes[1].imshow(mascara_real.squeeze().numpy(), cmap='gray')
    axes[1].set_title("Máscara Real")
    axes[2].imshow(pred_bin.squeeze().numpy(), cmap='gray')
    axes[2].set_title("Máscara Predita")
    
    # Overlay
    overlay = img.permute(1,2,0).numpy().copy()
    overlay[pred_bin.squeeze().numpy() > 0] = [255, 0, 0]  # Vermelho
    axes[3].imshow(overlay)
    axes[3].set_title("Overlay")
    
    plt.tight_layout()
    plt.show()
```

**O que observar:**
* Bordas mal definidas → modelo precisa de mais dados ou imagens maiores
* Buracos dentro de objetos → post-processing (preenchimento morfológico)
* Falsos positivos em textura → dataset mais variado

---

## 🔹 BLOCO 6 — MÉTRICAS DE SEGMENTAÇÃO

### IoU por Pixel (Jaccard Index)

```python
def iou_score(pred, target, threshold=0.5):
    pred_bin = (torch.sigmoid(pred) > threshold).float()
    intersecao = (pred_bin * target).sum()
    uniao = pred_bin.sum() + target.sum() - intersecao
    return (intersecao + 1e-6) / (uniao + 1e-6)
```

### Dice Coefficient (F1 de pixels)

```python
def dice_score(pred, target, threshold=0.5):
    pred_bin = (torch.sigmoid(pred) > threshold).float()
    intersecao = (pred_bin * target).sum()
    return (2 * intersecao + 1e-6) / (pred_bin.sum() + target.sum() + 1e-6)
```

### Pixel Accuracy

```python
def pixel_accuracy(pred, target, threshold=0.5):
    pred_bin = (torch.sigmoid(pred) > threshold).float()
    return (pred_bin == target).float().mean()
```

### 🎯 Interpretação

| Métrica | Bom | Aceitável |
|---|---|---|
| IoU (segmentação médica) | > 0.85 | > 0.70 |
| Dice | > 0.90 | > 0.75 |
| IoU (segmentação geral) | > 0.70 | > 0.55 |

---

## 🔹 BLOCO 7 — PÓS-PROCESSAMENTO

```python
import cv2

def pos_processar_mascara(mascara_bin):
    """Limpar máscara após threshold."""
    # Remover pequenos ruídos
    kernel = np.ones((5,5), np.uint8)
    sem_ruido = cv2.morphologyEx(mascara_bin, cv2.MORPH_OPEN, kernel)
    
    # Fechar buracos dentro de objetos
    fechada = cv2.morphologyEx(sem_ruido, cv2.MORPH_CLOSE, kernel)
    
    # Dilatação leve nas bordas
    dilatada = cv2.dilate(fechada, kernel, iterations=1)
    
    return dilatada

# Usar após predição do modelo
pred_np = (torch.sigmoid(pred) > 0.5).squeeze().numpy().astype(np.uint8)
pred_limpa = pos_processar_mascara(pred_np)
```

**Operações morfológicas:**
* **Erosão:** Remove pixels de borda (elimina ruídos finos)
* **Dilatação:** Adiciona pixels de borda (expande regiões)
* **Opening (erosão + dilatação):** Remove ruído sem mudar forma
* **Closing (dilatação + erosão):** Fecha buracos sem mudar forma

---

## 🔹 BLOCO 8 — MASK R-CNN (SEGMENTAÇÃO DE INSTÂNCIAS)

> Mask R-CNN combina detecção com segmentação. É mais complexo que U-Net — proporcional ao que resolve.

### Componentes

```
Imagem
  ↓
Backbone (ResNet + FPN)        ← Extrai features multi-escala
  ↓
Region Proposal Network (RPN)  ← Propõe ~2000 regiões candidatas
  ↓
ROI Align                      ← Extrai features fixas por região
  ↓
┌─────────────────────────────┐
│ Head de Classificação       │ ← Qual classe?
│ Head de Bbox                │ ← Refinar posição?
│ Head de Máscara (FCN 14×14) │ ← Máscara dentro do bbox?
└─────────────────────────────┘
```

### Uso com Detectron2 ou torchvision

```python
import torchvision
from torchvision.models.detection import maskrcnn_resnet50_fpn

model = maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

with torch.no_grad():
    predictions = model([img_tensor])

masks = predictions[0]['masks']       # (N, 1, H, W)
labels = predictions[0]['labels']     # (N,) classes
scores = predictions[0]['scores']     # (N,) confiança

# Filtrar por confiança
threshold = 0.5
keep = scores > threshold
masks = masks[keep].squeeze(1)        # (N_filtered, H, W)
```

### Quando usar Mask R-CNN vs U-Net

| Cenário | Recomendação |
|---|---|
| Segmentar 1 tipo de objeto (ex: tumor) | U-Net |
| Segmentar múltiplos objetos distintos | Mask R-CNN |
| Precisa de ID único por instância | Mask R-CNN |
| Dataset pequeno (<1000 imagens) | U-Net com transfer learning |
| Dataset grande, precisão máxima | Mask R-CNN ou PointRend |

---

## 🔹 BLOCO 9 — FOUNDATION MODELS DE SEGMENTAÇÃO: SAM / SAM2 🆕 (Adição desta revisão)

> ⚠️ **Por que este bloco existe:** U-Net e Mask R-CNN (Blocos 4 e 8) ensinam o **fundamento** — treinar um modelo para segmentar UMA classe específica que você define e anota. Isso continua sendo essencial. Mas desde 2023, existe um paradigma diferente que dominou boa parte da indústria: segmentação **promptable** e **zero-shot** — segmentar **qualquer objeto**, sem nunca ter treinado especificamente para aquela classe. Ignorar isso deixaria um buraco real no currículo.
>
> ⚠️ **Nota de validação temporal:** confirme rapidamente se SAM2 (ou um sucessor mais recente) é o que está em uso corrente no momento do seu estudo — esta é uma área de fronteira que evolui rápido.

### A Mudança de Paradigma

```
Paradigma clássico (U-Net, Mask R-CNN):
  "Treine um modelo para segmentar EXATAMENTE a classe 'tumor'"
  → Precisa de centenas/milhares de máscaras anotadas daquela classe específica

Paradigma SAM (Segment Anything):
  "Aqui está um ponto, uma caixa, ou uma região aproximada — segmente o que tem ali"
  → Funciona em objetos que o modelo NUNCA viu durante treino (zero-shot)
```

Isso foi possível porque o SAM original foi treinado no dataset **SA-1B**, com mais de 1 bilhão de máscaras — e a chave é que o dataset é **class-agnostic**: o modelo aprendeu o conceito geral de "o que é um objeto" e "onde estão suas bordas", não uma lista fixa de categorias.

### Arquitetura (Visão de Engenheiro)

```
Imagem → Image Encoder (ViT pesado, roda 1x por imagem)  → embedding da imagem
                                                                   ↓
Prompt (ponto, caixa, ou máscara aproximada) → Prompt Encoder    ↓
                                                                   ↓
                                          Mask Decoder (leve, roda rápido)
                                                                   ↓
                                                    Máscara(s) candidata(s) + score
```

**Por que isso é relevante de engenharia:** o encoder de imagem é pesado e só precisa rodar **uma vez por imagem**. Depois disso, você pode gerar várias máscaras diferentes (mudando o prompt) quase instantaneamente — isso é o que torna o SAM viável para uso interativo (clicar na imagem e ver a máscara aparecer em tempo real).

### Tipos de Prompt

| Tipo de prompt | Uso típico |
|---|---|
| **Point** (1 clique no objeto) | Interface interativa, anotação assistida |
| **Box** (bounding box aproximada) | Combinar com um detector (YOLO/RT-DETR da Fase 07) que já encontrou "onde", e SAM refina "qual o contorno exato" |
| **Texto** (via Grounding DINO + SAM) | "segmente o cachorro" sem clicar — combina detecção guiada por texto com segmentação |
| **Máscara grosseira** | Refinar uma máscara que você já tem (ex: saída ruidosa de outro modelo) |

### Uso Prático

```python
from ultralytics import SAM

# SAM via Ultralytics (mesma API que você já usa para YOLO)
model = SAM("sam2_b.pt")

# Prompt por ponto
resultado = model("imagem.jpg", points=[[400, 300]], labels=[1])

# Prompt por bounding box (ex: vinda de um detector YOLO treinado na Fase 07)
resultado = model("imagem.jpg", bboxes=[[120, 80, 350, 400]])

resultado[0].show()
masks = resultado[0].masks.data  # (N, H, W)
```

```python
# Combinando detector + SAM: "detecte e depois refine o contorno exato"
from ultralytics import YOLO, SAM

detector = YOLO("meu_detector.pt")   # da Fase 07
segmentador = SAM("sam2_b.pt")

deteccoes = detector("imagem.jpg")
bboxes = deteccoes[0].boxes.xyxy.tolist()

mascaras = segmentador("imagem.jpg", bboxes=bboxes)
```

### Quando SAM NÃO substitui U-Net/Mask R-CNN treinada especificamente

| Cenário | Recomendação |
|---|---|
| Domínio muito específico e fino (ex: limites exatos de tumor em corte histológico, onde a "borda certa" exige conhecimento de domínio que o SAM genérico não tem) | U-Net especializada treinada no seu domínio ainda vence em precisão |
| Você já tem milhares de máscaras anotadas e precisão é crítica | Modelo especializado (Bloco 4/8) — SAM é generalista, não foi otimizado para o seu caso específico |
| Prototipagem rápida, anotação assistida, ou domínio aberto (qualquer objeto comum) | SAM/SAM2 — zero-shot economiza semanas de anotação |
| Você precisa de **rótulo de classe** junto da máscara (SAM não classifica, só segmenta) | Combinar SAM com um classificador/detector downstream, ou usar Grounding DINO + SAM para segmentação guiada por texto |

### 🎯 Domínio

* Entender a diferença entre "treinar para uma classe" (Blocos 4/8) e "segmentar qualquer coisa sem treinar" (este bloco)
* Saber quando vale usar SAM para **acelerar a própria anotação** dos seus datasets de U-Net/Mask R-CNN — esse é um uso de produção real: gerar máscaras candidatas com SAM, revisar rapidamente, e usar como ground truth para treinar um modelo especializado mais leve depois.

### 🚧 Mini-projeto obrigatório

1. Pegar 10-20 imagens de um dataset que você já anotou manualmente nesta fase (Bloco 2)
2. Gerar máscaras com SAM usando prompts de bounding box (reaproveitando bboxes da Fase 07, se tiver)
3. Comparar visualmente: máscara do SAM vs. sua máscara anotada manualmente
4. Medir IoU entre as duas (reaproveitando a função do Bloco 6)
5. **Reflexão escrita:** em quais casos o SAM bateu sua anotação manual, e em quais errou? Isso é exatamente o tipo de análise que vira parágrafo de "Limitações Conhecidas" no README de portfólio (Fase 12)

---

## 🧪 PROJETOS OBRIGATÓRIOS

### 1️⃣ Remoção de Fundo

* Segmentar objeto principal
* Aplicar máscara para remover fundo
* Substituir por fundo novo ou transparente (PNG com alpha)

### 2️⃣ U-Net do Zero

* Dataset simples (ex: Oxford Pets, Carvana, ou dataset próprio)
* Treino completo com BCE + Dice
* Avaliação: IoU e Dice por época (plotar curvas)
* Meta: IoU > 0.80

### 3️⃣ Segmentação Multi-Classe

* Pelo menos 3 classes + fundo
* Usar cross-entropy para multi-classe
* Avaliar mIoU (mean IoU sobre todas as classes)

### 4️⃣ Medição de Área

* Segmentar objeto
* Contar pixels da máscara
* Converter pixels para área real (se escala conhecida)

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Tipos de segmentação (semântica, instância, panóptica)
2. Representação de máscara (binária, multi-classe, one-hot)
3. Dataset imagem/máscara (estrutura + alinhamento)
4. Dataset PyTorch customizado com augmentation correto
5. Loss functions (BCE, Dice, Focal)
6. U-Net (implementar do zero)
7. Treinar U-Net em dataset simples
8. Visualização e debug de predições
9. Métricas: IoU, Dice, pixel accuracy
10. Pós-processamento morfológico
11. Mask R-CNN (uso, não implementação do zero)
12. 🆕 SAM/SAM2: prompts (ponto, box, texto via Grounding DINO) e uso prático
13. 🆕 Comparar SAM vs. anotação manual (IoU) e usar SAM para acelerar anotação
14. **Projetos obrigatórios**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Não alinhar imagem e máscara (erros silenciosos devastadores)
* Aplicar flip na imagem mas não na máscara (destroi o treino)
* Não visualizar resultado intermediário durante treino
* Usar só pixel accuracy (inútil com classes desbalanceadas)
* Pular U-Net e ir direto para Mask R-CNN

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 09 se:

* [ ] Treina U-Net do zero com IoU > 0.80
* [ ] Entende pixel-level prediction (cada pixel tem gradiente)
* [ ] Avalia com IoU e Dice corretamente
* [ ] Aplica pós-processamento morfológico para melhorar máscara
* [ ] Segmenta múltiplos objetos de instâncias diferentes com Mask R-CNN
* [ ] Cria dataset próprio de segmentação com anotação manual
* [ ] 🆕 Usa SAM/SAM2 com prompts de ponto e box, e explica quando SAM substitui (ou não) um modelo especializado


---
