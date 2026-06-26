# FASE 07 — OBJECT DETECTION

> **Posição na trilha:** Evolução de classificação para localização — agora o modelo diz "onde" além de "o quê".
> **Nível:** Avançado
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fases 05 (CNN sólida) e 06 (Transformers para contexto de DETR)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### CNN (Fase 05 sólida)

* Convolução, feature maps, pooling
* Controle de shape
* Transfer learning

### Imagem e Vídeo (Fase 03)

* OpenCV: leitura de imagem e vídeo, frame a frame
* **Fase 03 Bloco 4 (vídeo) é explicitamente necessário** — tracking usa `VideoCapture`

### Treinamento de Modelos

* Dataset → treino → validação
* Overfitting, métricas (precision, recall, F1)

### Estrutura de Projeto

* Separação: `data/`, `train/`, `inference/`

---

## 🔹 BLOCO 1 — CONCEITOS FUNDAMENTAIS

### O que é Object Detection?

**Classificação:** "Esta imagem contém um gato" (1 resposta por imagem)  
**Detection:** "Há um gato em [x:230, y:120, w:80, h:90] e um cachorro em [x:400, y:200, w:100, h:95]"

Saída = lista de `(classe, bounding_box, confiança)` por objeto

### Bounding Box (Bbox)

**Formato Pascal VOC (absoluto):**
```
(x_min, y_min, x_max, y_max)
Exemplo: (120, 80, 250, 200)  ← pixels absolutos
```

**Formato YOLO (normalizado):**
```
(x_center, y_center, width, height)
Valores entre 0 e 1 (relativos ao tamanho da imagem)
Exemplo: (0.48, 0.54, 0.32, 0.45)
```

**Conversão:**
```python
def pascal_to_yolo(x_min, y_min, x_max, y_max, img_w, img_h):
    x_center = (x_min + x_max) / 2 / img_w
    y_center = (y_min + y_max) / 2 / img_h
    width = (x_max - x_min) / img_w
    height = (y_max - y_min) / img_h
    return x_center, y_center, width, height
```

### IoU (Intersection over Union)

```python
def calcular_iou(box1, box2):
    """
    box1, box2: (x1, y1, x2, y2)
    """
    # Área de interseção
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    intersecao = max(0, x2 - x1) * max(0, y2 - y1)
    
    # Área de cada bbox
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    
    uniao = area1 + area2 - intersecao
    
    return intersecao / (uniao + 1e-6)
```

**Interpretação:**
* IoU > 0.5: detecção razoável (limiar mais comum)
* IoU > 0.75: detecção precisa
* IoU = 1.0: perfeito (bbox idêntico ao ground truth)

### mAP (mean Average Precision)

* A métrica padrão da indústria para detecção
* Para cada classe: calcular Average Precision (área sob curva Precision-Recall)
* mAP = média das APs de todas as classes

```
mAP@0.5     → IoU threshold = 0.5
mAP@0.5:0.95 → média de IoUs de 0.5 a 0.95 (mais rigoroso — padrão COCO)
```

### 🎯 Domínio

* Avaliar modelo corretamente — não só "parece bom" visualmente

### 🚧 Exercício

* Calcular IoU manual com dois bboxes
* Implementar NMS (Non-Maximum Suppression): quando múltiplas detecções se sobrepõem, manter só a de maior confiança

---

## 🔹 BLOCO 2 — PIPELINE DE DATASET (CRÍTICO)

> A qualidade do dataset define o teto de qualidade do modelo. Treinar com dataset ruim = perder tempo.

### Etapas Reais de um Projeto de Detecção

```
1. Definir problema          ← O que detectar? Quantas classes?
2. Coletar imagens            ← Fonte: Kaggle, Roboflow, captura própria
3. Anotar (rotular)           ← Desenhar bboxes + classe
4. Dividir dataset            ← 70% train, 20% val, 10% test
5. Treinar modelo             ← YOLO ou similar
6. Avaliar (mAP, PR curve)    ← Não apenas olhar imagem
7. Analisar erros             ← Onde o modelo erra?
8. Iterar (mais dados / ajuste) ← Ciclo contínuo
9. Deploy                     ← API, edge, webcam
```

### Ferramentas de Anotação

**LabelImg** — local, simples, gratuito
```bash
pip install labelImg
labelImg
```

**Roboflow** — web, colaborativo, exporta em vários formatos
* Exporta diretamente em formato YOLO
* Augmentation automático
* Versionamento de dataset

### Estrutura de Dataset YOLO

```
dataset/
├── images/
│   ├── train/      ← 70% das imagens
│   │   ├── img001.jpg
│   │   └── img002.jpg
│   └── val/        ← 20% das imagens
│       └── img003.jpg
├── labels/
│   ├── train/      ← Mesmo nome das imagens, extensão .txt
│   │   ├── img001.txt
│   │   └── img002.txt
│   └── val/
│       └── img003.txt
└── data.yaml       ← Configuração do dataset
```

**Arquivo .txt (label YOLO):**
```
# Formato: classe x_center y_center width height (todos normalizados 0-1)
0 0.480 0.540 0.320 0.450    ← classe 0 (ex: pessoa)
1 0.750 0.320 0.150 0.280    ← classe 1 (ex: carro)
```

**data.yaml:**
```yaml
train: ./images/train
val: ./images/val
nc: 2                          # número de classes
names: ['pessoa', 'carro']
```

### Boas Práticas de Dataset

* **Variedade:** diferentes ângulos, iluminações, fundos, escalas
* **Balanceamento:** classes similares em quantidade
* **Qualidade da anotação:** bbox justo ao objeto (não muito grande, não muito pequeno)
* **Mínimo prático:** 200+ imagens por classe para começar

---

## 🔹 BLOCO 3 — COMO FUNCIONAM OS DETECTORES

### Two-Stage Detectors (Mais Precisos, Mais Lentos)

**R-CNN → Fast R-CNN → Faster R-CNN (progressão)**

```
Imagem
  ↓
Region Proposal Network (RPN)  ← Propõe ~2000 regiões candidatas
  ↓
ROI Pooling / ROI Align        ← Extrai features de cada região
  ↓
Classificação + Refinamento de bbox
```

**Quando usar:** Precisão máxima > velocidade (ex: análise médica, inspeção industrial)

### One-Stage Detectors (Mais Rápidos, Competitivos em Precisão)

**YOLO, SSD, RetinaNet**

```
Imagem
  ↓
Backbone (CNN/ViT)             ← Extrai features
  ↓
Grid de predições              ← Cada célula do grid prediz bboxes + classes
  ↓
NMS                            ← Remove duplicatas
```

> 🛠️ **Correção desta revisão:** o termo correto é **RetinaNet** — o modelo que introduziu a **Focal Loss** como solução para desbalanceamento extremo entre fundo e objeto em detectores one-stage. "RetinaFocal Loss" não é um nome de modelo nem de loss — são dois conceitos diferentes que não devem ser fundidos: RetinaNet é a arquitetura, Focal Loss é a função de perda que ela usa (já vista na Fase 08, Bloco 3, no contexto de segmentação).

**Quando usar:** Velocidade importante (webcam, edge, vídeo em tempo real)

### DETR (Detection Transformer) — Contexto

* Usa Transformer (atenção) para detecção
* Não precisa de NMS (atenção aprende a não duplicar)
* Requer mais dados e treino mais longo
* **Relevante com a Fase 06** — atenção cross entre features da imagem e queries de objeto

#### 🆕 RT-DETR vs YOLO — Comparação Prática (Adição desta revisão)

> O roadmap original cita DETR apenas como "contexto" e nunca volta a ele como exercício. Isso deixa uma pergunta de entrevista sem resposta prática: **"quando você NÃO usaria YOLO?"** — a resposta certa é justamente quando NMS começa a falhar.

**Por que NMS falha em certos cenários:**
* Objetos densos e sobrepostos (ex: pessoas em multidão, produtos empilhados em gôndola) — NMS pode descartar uma detecção correta só porque o IoU com outra bbox vizinha passou do threshold.
* DETR-family (incluindo variantes em tempo real como **RT-DETR**) aprende via atenção a não duplicar detecções — elimina a necessidade de NMS e do hiperparâmetro de threshold associado.

**Exercício prático recomendado:**
1. Treinar **RT-DETR** no mesmo dataset usado para treinar YOLO neste bloco (mesma divisão treino/val)
2. Comparar três eixos: **mAP**, **latência** (FPS), e **comportamento em objetos sobrepostos** (escolher imagens do seu dataset com objetos próximos/sobrepostos e comparar visualmente as detecções de cada modelo)
3. Usar via Ultralytics (que já empacota RT-DETR com a mesma API do YOLO):
```python
from ultralytics import RTDETR

model = RTDETR("rtdetr-l.pt")
model.train(data="data.yaml", epochs=100, imgsz=640)
metrics = model.val()
```

**🎯 Domínio esperado:** Conseguir argumentar com dados próprios (não teoria) em qual cenário cada arquitetura ganha — isso é exatamente o tipo de resposta que demonstra maturidade técnica em entrevista.

> ⚠️ **Nota de validação temporal:** o ecossistema de detectores muda rápido. Antes de investir tempo de treino, confirme rapidamente se RT-DETR continua sendo a opção transformer-based real-time mais madura no momento do seu estudo, ou se surgiu sucessor mais relevante.

---

## 🔹 BLOCO 4 — YOLO NA PRÁTICA

### Por que YOLO?

* Mais rápido da categoria one-stage
* Ultraltyics YOLO = melhor DX da indústria
* YOLOv8/YOLOv11: estado da arte em velocidade/precisão

> 🛠️ **Nota de validação temporal (esta revisão):** números de versão específicos (YOLOv8, YOLOv11...) ficam desatualizados rápido — a Ultralytics lança novas versões com frequência. Antes de treinar, **confira no repositório oficial da Ultralytics qual é a versão estável mais recente no momento do seu estudo** em vez de fixar mentalmente um número de versão deste documento. O que não muda é a API (`YOLO(...)`, `.train()`, `.val()`, `.predict()`) — o código abaixo continua válido independentemente da versão exata.

```python
from ultralytics import YOLO

# Usar modelo pré-treinado
model = YOLO("yolov8n.pt")  # n=nano, s=small, m=medium, l=large, x=extra

# Inferência
results = model("imagem.jpg")
for r in results:
    print(r.boxes)           # Bboxes detectados
    print(r.boxes.cls)       # Classes
    print(r.boxes.conf)      # Confiança
    r.show()                 # Visualizar

# Inferência em vídeo
results = model("video.mp4", stream=True)
for r in results:
    frame_anotado = r.plot()
    cv2.imshow("Detecção", frame_anotado)
```

### Treinar YOLO com Dataset Próprio

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Inicializa com pesos pré-treinados

# Treinar
results = model.train(
    data="data.yaml",        # Arquivo de configuração do dataset
    epochs=100,
    imgsz=640,               # Tamanho da imagem
    batch=16,
    device=0,                # GPU (0) ou cpu
    lr0=0.01,
    patience=20,             # Early stopping se não melhorar em 20 epochs
    save=True
)

# Avaliar
metrics = model.val()
print(f"mAP@0.5: {metrics.box.map50:.3f}")
print(f"mAP@0.5:0.95: {metrics.box.map:.3f}")
```

### 🎯 Domínio

* Treinar modelo do zero **sem tutorial**

---

## 🔹 BLOCO 5 — PROJETOS OBRIGATÓRIOS DE DETECÇÃO

### 1️⃣ Detecção em Webcam (Tempo Real)

```python
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    results = model(frame, stream=False)
    frame_anotado = results[0].plot()
    cv2.imshow("Detecção", frame_anotado)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
```

### 2️⃣ Multi-Classes (pessoa + carro + moto)

* Dataset público (ex: COCO subset)
* Avaliação por classe separada (mAP por classe)

### 3️⃣ Dataset Próprio (CRÍTICO)

**Sugestão de problema:** Capacete vs sem capacete (EPI industrial), Cinto de segurança, Produto com defeito, Seu próprio problema

* Coletar 200+ imagens por classe
* Anotar com Roboflow ou LabelImg
* Treinar e atingir mAP@0.5 > 0.75

### 4️⃣ Salvar Vídeo com Detecção

```python
model = YOLO("meu_modelo.pt")
results = model.predict("entrada.mp4", save=True, project="saidas/")
```

---

## 🔹 BLOCO 6 — TRACKING

> Detecção identifica objetos em cada frame independentemente. Tracking associa o **mesmo objeto** ao longo de múltiplos frames.

### Por que Tracking?

Detecção pura: "frame 1: pessoa A em posição X; frame 2: pessoa A ainda em posição X?" — sem tracking, são dois objetos diferentes.

### SORT (Simple Online and Realtime Tracking)

* Associa detecções entre frames usando IoU + filtro de Kalman
* Muito rápido, funciona sem GPU adicional

### DeepSORT

* SORT + features visuais (embedding)
* Mais robusto a oclusões (objeto some e volta)

### BoT-SORT / ByteTrack (Estado da Arte)

* Atual padrão da indústria
* Integrado ao Ultralytics YOLO:

```python
results = model.track("video.mp4", persist=True, tracker="bytetrack.yaml")

for r in results:
    for box in r.boxes:
        track_id = box.id.int()      # ID único e persistente do objeto
        cls = box.cls.int()
        print(f"Objeto {track_id}: classe {cls}")
```

### 🚧 Mini-projeto

* Contar pessoas entrando e saindo de uma área
* Contar veículos passando por linha virtual

---

## 🔹 BLOCO 7 — OTIMIZAÇÃO E DEPLOY

### Exportação de Modelo

```python
# ONNX (compatível com múltiplos runtimes)
model.export(format="onnx", opset=11)

# TensorRT (máxima performance em GPU NVIDIA)
model.export(format="engine", device=0)

# INT8 (quantização — menor tamanho, mais rápido, leve perda de precisão)
model.export(format="engine", int8=True, data="data.yaml")
```

### Benchmark de Performance

```python
# Medir FPS real
import time

cap = cv2.VideoCapture("video.mp4")
frames = 0
start = time.time()

while True:
    ret, frame = cap.read()
    if not ret: break
    model(frame)
    frames += 1

fps = frames / (time.time() - start)
print(f"FPS: {fps:.1f}")
```

### Edge (Hardware Específico)

**Raspberry Pi:** Usar modelo nano (n) exportado em ONNX  
**NVIDIA Jetson:** Exportar para TensorRT (.engine)  
**Apple Silicon (M1/M2):** Exportar para CoreML

---

## 🔹 BLOCO 8 — DEBUG E MELHORIA DE MODELO

### Diagnóstico por Curvas

Ultralytics gera automaticamente:
* **P-R Curve:** Relação precision/recall em vários thresholds
* **F1 Curve:** Melhor threshold de confiança
* **Confusion Matrix:** Onde o modelo confunde classes

### Problemas Comuns e Soluções

| Problema | Sintoma | Solução |
|---|---|---|
| Overfitting | mAP treino >> val | Mais dados, augmentation |
| Underfitting | mAP baixo em treino | Modelo maior, mais épocas |
| Muitos falsos positivos | Precisão baixa | Aumentar threshold de confiança |
| Muitos falsos negativos | Recall baixo | Mais dados positivos |
| Confusão entre classes | Diagonal da conf. matrix não dominante | Mais diversidade no dataset |

---

## 🔹 BLOCO 9 — OCR: DETECÇÃO E RECONHECIMENTO DE TEXTO 🆕 (Adição desta revisão)

> Leitura de texto em imagem (placas, documentos, etiquetas, notas fiscais) é uma das aplicações comerciais mais comuns de visão computacional, e aparecia nos projetos de portfólio sugeridos da Fase 12 (leitura de placa) sem nunca ter sido ensinada tecnicamente. Este bloco fecha essa lacuna.

### Por que OCR é "Detecção + algo mais"

OCR raramente é um modelo único — é um **pipeline de dois estágios**, o que conecta diretamente com tudo que você aprendeu nesta fase:

```
Imagem completa
    ↓
1. Detecção de região de texto    ← Onde está o texto? (bounding box ou polígono)
    ↓
2. Recorte da região
    ↓
3. Reconhecimento de caractere     ← O que está escrito ali?
    ↓
Texto final (string)
```

### Abordagem Clássica (mais leve, boa para texto bem definido)

```python
import pytesseract
from PIL import Image

# Detecção de texto: usar seu detector da Fase 07 (YOLO treinado para
# a classe "placa" ou "região de texto"), depois recortar e passar ao OCR
img_recortada = img.crop((x1, y1, x2, y2))  # bbox do detector

texto = pytesseract.image_to_string(img_recortada, lang="por")
print(texto.strip())
```

**Quando funciona bem:** texto impresso, alto contraste, ângulo reto, fonte padrão (documentos, notas fiscais escaneadas).
**Quando falha:** texto manuscrito, ângulo/perspectiva, baixa resolução, fontes decorativas, placas sujas/desgastadas.

### Abordagem Moderna (Transformer-based — mais robusta)

Para os casos onde o Tesseract falha, modelos baseados em Transformer tratam reconhecimento de texto como tradução de imagem para sequência (similar a um encoder-decoder de NLP, conectando com a Fase 06):

```python
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-printed")

img = Image.open("placa_recortada.jpg").convert("RGB")
pixel_values = processor(images=img, return_tensors="pt").pixel_values

ids_gerados = model.generate(pixel_values)
texto = processor.batch_decode(ids_gerados, skip_special_tokens=True)[0]
print(texto)
```

**Ferramentas alternativas de produção:** PaddleOCR (open-source, multilíngue, detecção+reconhecimento integrados) e EasyOCR (boa relação simplicidade/robustez para prototipagem rápida).

### 🎯 Domínio

* Entender que OCR robusto = "seu próprio detector" (Fase 07) + um reconhecedor de texto — não um modelo mágico único
* Saber escolher: Tesseract (rápido, leve, texto limpo) vs TrOCR/PaddleOCR (mais robusto, mais pesado)

### 🚧 Exercício obrigatório

* Treinar (ou reaproveitar) um detector YOLO para a classe "placa" ou "região de texto"
* Recortar a região detectada e rodar Tesseract e TrOCR no mesmo recorte
* Comparar acurácia de transcrição entre os dois em pelo menos 20 imagens reais (idealmente capturadas por você)

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Bounding box formatos (Pascal VOC, YOLO)
2. IoU manual (implementar)
3. NMS (implementar conceitual)
4. mAP (entender, usar ferramenta)
5. Pipeline de dataset (coletar → anotar → dividir)
6. Estrutura YOLO de dataset + data.yaml
7. Treinar YOLO com dataset público
8. Inferência: imagem → vídeo → webcam
9. Dataset próprio (anotar + treinar)
10. Avaliação: mAP, curvas, confusion matrix
11. 🆕 Treinar RT-DETR no mesmo dataset e comparar com YOLO
12. Tracking com ByteTrack
13. Exportar ONNX / TensorRT
14. Debug e melhoria
15. 🆕 OCR: pipeline detecção + reconhecimento (Tesseract e/ou TrOCR)

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Não anotar dataset próprio (usar só datasets prontos)
* Usar só modelo pré-treinado sem fine-tuning
* Ignorar métricas — mAP importa, não só "parece bom visualmente"
* Dataset pequeno e pouco variado (> 200 imagens por classe é mínimo)
* Não validar em dados que o modelo nunca viu

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 08 se:

* [ ] Treina detector YOLO do zero com dataset próprio
* [ ] Avalia com mAP@0.5 e interpreta confusion matrix
* [ ] Detecta em vídeo em tempo real com fps aceitável
* [ ] Implementa tracking e conta objetos ao longo do tempo
* [ ] Consegue melhorar mAP sistematicamente (não aleatoriamente)
* [ ] 🆕 Compara YOLO com RT-DETR no mesmo dataset e explica em que cenário cada um ganha


---
