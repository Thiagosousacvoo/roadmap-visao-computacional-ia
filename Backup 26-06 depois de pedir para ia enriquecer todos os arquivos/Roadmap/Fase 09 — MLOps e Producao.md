# FASE 09 — MLOPS E PRODUÇÃO

> **Posição na trilha:** Transforma modelo em produto real. Aqui o modelo sai do notebook e entra no mundo.
> **Nível:** Profissional (engenharia de sistemas)
> **Tempo estimado:** 2–3 semanas (dedicação intensiva de 8–12h/dia) — 🛠️ ajustado nesta revisão (era 1-2 semanas) para acomodar quantização real, robustez e testes/CI
> **Pré-requisito:** Fases 07 ou 08 — ter um modelo funcional (YOLO ou U-Net)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Modelos Treinados (Fase 07 ou 08)

* Ter um modelo funcional: YOLO (detecção) OU U-Net (segmentação)
* Saber salvar/carregar: `torch.save()`, `torch.load()`
* Inferência em modo eval

### Backend Mínimo

* HTTP (GET/POST)
* JSON: estruturar e parsear

### Linux + CLI

* Rodar scripts via terminal
* Variáveis de ambiente (`export`, `.env`)

### Git

* Versionar projeto completo
* `.gitignore` correto (não commitar modelo .pth gigante)

---

## 🔹 BLOCO 1 — SERVING (API DE MODELO)

> 🔧 **Execução obrigatória** — você sai com uma API funcional

### Por que FastAPI?

* Mais rápido que Flask para I/O async
* Documentação automática (`/docs`)
* Validação de tipos nativa (Pydantic)
* Padrão da indústria para ML APIs

### API Mínima Funcional

```python
# api.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torch, cv2, numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI(title="API de Visão Computacional")

# Carregar modelo UMA VEZ na inicialização
from ultralytics import YOLO
model = YOLO("modelos/detector.pt")
model.to("cuda" if torch.cuda.is_available() else "cpu")

@app.post("/detectar")
async def detectar(file: UploadFile = File(...)):
    # Ler imagem do upload
    contents = await file.read()
    img = Image.open(BytesIO(contents)).convert("RGB")
    img_np = np.array(img)
    
    # Inferência
    results = model(img_np)
    
    # Formatar resposta
    deteccoes = []
    for box in results[0].boxes:
        deteccoes.append({
            "classe": model.names[int(box.cls)],
            "confianca": float(box.conf),
            "bbox": box.xyxy[0].tolist()  # [x1, y1, x2, y2]
        })
    
    return JSONResponse({"deteccoes": deteccoes, "total": len(deteccoes)})

@app.get("/health")
async def health():
    return {"status": "ok", "modelo": "detector_v1"}
```

```bash
# Rodar
uvicorn api:app --host 0.0.0.0 --port 8000 --reload

# Testar
curl -X POST "http://localhost:8000/detectar" \
     -H "accept: application/json" \
     -F "file=@foto.jpg"
```

### Erros Comuns em APIs de Visão

* Carregar modelo a cada request → latência enorme (carregar na inicialização)
* Não validar formato/tamanho da imagem → crash com entrada inválida
* Resposta sem timeout → request pendente para sempre

---

## 🔹 BLOCO 2 — CONTAINERIZAÇÃO (DOCKER)

> 🔧 **Execução obrigatória** — você sai com container funcionando

### Por que Docker?

* "Funciona na minha máquina" → eliminado
* Reproducibilidade: mesmo ambiente em qualquer servidor
* Padrão de todo deploy em cloud

### Dockerfile para API de Visão

```dockerfile
# Fase 1: Imagem base
FROM python:3.11-slim

# Instalar dependências do sistema (OpenCV precisa disso)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxext6 libxrender-dev libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Instalar dependências Python (antes de copiar código — aproveita cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Expor porta
EXPOSE 8000

# Comando de inicialização
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build
docker build -t api-visao:v1 .

# Run (CPU)
docker run -p 8000:8000 api-visao:v1

# Run (GPU)
docker run --gpus all -p 8000:8000 api-visao:v1

# Verificar se está rodando
curl http://localhost:8000/health
```

### Docker Compose (API + Workers + Redis)

```yaml
# docker-compose.yml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./modelos:/app/modelos
    environment:
      - MODEL_PATH=/app/modelos/detector.pt
    depends_on:
      - redis
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
```

---

## 🔹 BLOCO 3 — PIPELINE DE INFERÊNCIA

> 🔧 **Execução obrigatória** — distingue conceito de execução real

### Síncrono (Padrão — para a maioria dos casos)

```
POST /detectar
    ↓
[Pré-processar] → [Modelo] → [Pós-processar] → Retorna JSON
```

Adequado para: < 500ms de processamento, < 100 req/s

### Assíncrono (Produção real com filas)

```
POST /analisar        ← Retorna imediatamente com job_id
    ↓
Redis/RabbitMQ        ← Fila de jobs
    ↓
Worker (separado)     ← Processa assincronamente
    ↓
GET /resultado/{id}   ← Cliente busca resultado
```

```python
# Simular fila com Redis + background tasks FastAPI
from fastapi import BackgroundTasks
import redis, json, uuid

r = redis.Redis(host='localhost', port=6379)

@app.post("/analisar-async")
async def analisar_async(file: UploadFile, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    contents = await file.read()
    
    # Salvar tarefa na fila
    r.set(f"job:{job_id}:status", "pending")
    background_tasks.add_task(processar_imagem, job_id, contents)
    
    return {"job_id": job_id, "status": "queued"}

async def processar_imagem(job_id: str, contents: bytes):
    r.set(f"job:{job_id}:status", "processing")
    # ... inferência aqui ...
    r.set(f"job:{job_id}:resultado", json.dumps(resultado))
    r.set(f"job:{job_id}:status", "done")

@app.get("/resultado/{job_id}")
async def resultado(job_id: str):
    status = r.get(f"job:{job_id}:status")
    if status == b"done":
        return json.loads(r.get(f"job:{job_id}:resultado"))
    return {"status": status.decode()}
```

---

## 🔹 BLOCO 4 — CLOUD (NOÇÃO PRÁTICA)

> 📖 **Conceito** — entender o que existe, não executar todos

### Opções de Deploy

**Heroku / Railway (mais simples)**
* Subir container diretamente
* Adequado para demonstração, não para produção escalável

**AWS EC2 + ECR**
* EC2: VM na cloud
* ECR: registry de containers (como Docker Hub privado)
* ECS: orquestrar containers

**AWS SageMaker**
* Endpoint gerenciado para modelos ML
* Auto-scaling automático
* Monitoramento integrado

**Google Cloud Run**
* Serverless — só paga quando recebe requisição
* Escala para zero quando não usado

### O que Você Precisa Saber

```
1. Subir container para registry (ECR, GCR)
2. Criar instância com GPU (se necessário)
3. Expor endpoint publicamente
4. Configurar auto-scaling (opcional)
```

**Exercício prático:** Deploy gratuito no Railway ou Fly.io com a API do Bloco 1

---

## 🔹 BLOCO 5 — VERSIONAMENTO DE DADOS E MODELOS

> 📖 **Conceito** + 🔧 **execução do projeto de versionamento**

### DVC (Data Version Control)

```bash
pip install dvc dvc-s3  # ou dvc-gdrive para Google Drive

# Inicializar
git init && dvc init

# Rastrear dataset
dvc add data/dataset/
git add data/dataset.dvc .gitignore
git commit -m "Adicionar dataset v1"

# Rastrear modelo
dvc add modelos/detector.pt
git commit -m "Modelo v1 treinado"

# Push para armazenamento remoto
dvc remote add myremote s3://meu-bucket/dvc
dvc push

# Recuperar versão específica
git checkout v1.0
dvc checkout
```

### Por que importa?

* Reproduzir experimento de 3 meses atrás
* Rollback de modelo que degradou em produção
* Colaborar em equipe sem versionar arquivo binário gigante no Git

### MLflow (Opcional, mas muito usado)

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("lr", 0.001)
    mlflow.log_param("epochs", 100)
    mlflow.log_metric("mAP@0.5", 0.823)
    mlflow.pytorch.log_model(model, "model")
```

---

## 🔹 BLOCO 6 — MONITORAMENTO (CRÍTICO)

> 🔧 **Execução obrigatória** — modelo sem monitoramento é modelo que vai degradar silenciosamente

### O que Monitorar

**Métricas de Sistema:**
* Latência por request (p50, p95, p99)
* Throughput (requests/segundo)
* Uso de CPU/GPU/memória

**Métricas de Modelo:**
* Distribuição das classes preditas
* Distribuição da confiança
* Taxa de requests com confiança < threshold

### Logging Estruturado

```python
import logging, json, time
from datetime import datetime

# Logger estruturado (JSON)
logger = logging.getLogger("api_visao")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(handler)

def log_predicao(request_id, num_deteccoes, classes, confidencias, latencia_ms):
    entrada = {
        "timestamp": datetime.utcnow().isoformat(),
        "request_id": request_id,
        "num_deteccoes": num_deteccoes,
        "classes": classes,
        "confianca_media": sum(confidencias) / max(len(confidencias), 1),
        "latencia_ms": latencia_ms
    }
    logger.info(json.dumps(entrada))

# No endpoint:
inicio = time.time()
resultado = model(img)
latencia = (time.time() - inicio) * 1000
log_predicao(request_id, len(resultado), classes, confianças, latencia)
```

### Data Drift (Degradação por Distribuição)

**O problema:** Modelo foi treinado em imagens de dia. Em produção, começam a chegar imagens de noite. Performance degrada sem nenhum erro.

**Detecção:**
* Monitorar: distribuição de brilho das imagens de entrada
* Monitorar: confiança média das predições
* Alertar: se confiança média cair abaixo de threshold por N horas consecutivas

### 🚧 Mini-projeto

* Logar todas as predições com classes, confiança e latência
* Criar script que lê logs e gera gráfico de distribuição de confiança ao longo do tempo

---

## 🔹 BLOCO 7 — ACTIVE LEARNING (MELHORAR MODELO CONTINUAMENTE)

> 🔧 **Execução obrigatória** — implementar ciclo completo uma vez

### Pipeline

```
1. Modelo em produção recebe imagem
2. Predição com baixa confiança → salvar imagem automaticamente
3. Batch semanal de imagens incertas vai para anotação
4. Anotar (Roboflow, CVAT)
5. Re-treinar modelo com dados novos
6. Validar: nova versão > versão anterior?
7. Deploy da nova versão
8. Repetir
```

### Implementação

```python
# Salvar automaticamente imagens onde modelo tem dúvida
CONFIANCA_MINIMA = 0.7
PASTA_REVISAO = "para_anotar/"

@app.post("/detectar")
async def detectar(file: UploadFile):
    # ... inferência ...
    
    confiancas = [d["confianca"] for d in deteccoes]
    if confiancas and max(confiancas) < CONFIANCA_MINIMA:
        # Salvar para revisão humana
        nome = f"{uuid.uuid4()}.jpg"
        with open(f"{PASTA_REVISAO}/{nome}", "wb") as f:
            f.write(contents)
        logger.info(f"Imagem incerta salva: {nome}")
```

---

## 🔹 BLOCO 8 — ESCALA E OTIMIZAÇÃO

### ONNX Runtime (CPU rápida)

```python
import onnxruntime as ort
import numpy as np

# Converter para ONNX
model.export(format="onnx")

# Usar ONNX Runtime (2-5x mais rápido que PyTorch CPU)
session = ort.InferenceSession("modelo.onnx", providers=['CPUExecutionProvider'])
input_name = session.get_inputs()[0].name
resultado = session.run(None, {input_name: img_array})
```

### TensorRT (GPU máxima performance)

```python
# Exportar (requer CUDA instalado)
model.export(format="engine", device=0, half=True)  # FP16

# Usar engine (3-5x mais rápido que PyTorch CUDA)
model_trt = YOLO("modelo.engine")
```

### Benchmark

```python
import time

def benchmark(model_func, img, n=100):
    # Warm-up
    for _ in range(5):
        model_func(img)
    
    inicio = time.perf_counter()
    for _ in range(n):
        model_func(img)
    total = time.perf_counter() - inicio
    
    return {"fps": n/total, "latencia_ms": (total/n)*1000}

print(benchmark(model_pytorch, img))
print(benchmark(model_onnx, img))
```

### 🆕 Quantização de Verdade: PTQ vs QAT (Adição desta revisão)

> O conteúdo original parava em "exportar para ONNX/TensorRT" sem entrar no que de fato acontece dentro da quantização nem no trade-off de precisão. Isso é exatamente o tipo de pergunta que separa quem "rodou o comando de export" de quem entende o que está fazendo — e é citado como prática padrão de mercado para sistemas de visão em tempo real e edge: escolher o menor modelo que ainda atende ao SLA de latência, e então comprimi-lo sem destruir a precisão.

**O que é quantização, de fato:**

Os pesos e ativações de uma rede normalmente são `float32` (32 bits). Quantização reduz a precisão numérica — geralmente para `int8` (8 bits) — o que reduz o tamanho do modelo em ~4x e acelera a inferência, especialmente em CPU e hardware de edge sem GPU dedicada.

```
FP32 (padrão treino)     → 4 bytes por peso, máxima precisão
FP16 (half precision)    → 2 bytes por peso, leve perda, padrão em GPU moderna
INT8 (quantizado)        → 1 byte por peso, maior perda, necessário em CPU/edge
```

**Post-Training Quantization (PTQ) — mais simples:**

```python
# Quantizar DEPOIS de já ter o modelo treinado em FP32
# Requer um "calibration dataset" — um pequeno conjunto representativo
# de imagens reais, usado para calibrar os ranges de quantização
model.export(format="engine", int8=True, data="data.yaml")  # Ultralytics já faz isso internamente

# Equivalente conceitual com ONNX Runtime:
from onnxruntime.quantization import quantize_static, CalibrationDataReader

# CalibrationDataReader: você implementa fornecendo batches do seu
# dataset real (não dados sintéticos) para calibrar os ranges int8
quantize_static("modelo.onnx", "modelo_int8.onnx", calibration_data_reader=meu_reader)
```

* **Vantagem:** rápido, não precisa re-treinar
* **Risco:** pode perder precisão de forma mais acentuada, especialmente em modelos pequenos ou tarefas sensíveis (ex: segmentação médica fina)

**Quantization-Aware Training (QAT) — mais robusto:**

```python
# QAT simula a quantização DURANTE o treino, deixando o modelo
# "se acostumar" com a perda de precisão e compensar nos pesos

import torch.quantization as tq

modelo.qconfig = tq.get_default_qat_qconfig('fbgemm')
modelo_preparado = tq.prepare_qat(modelo, inplace=False)

# Treinar (ou fine-tunar) normalmente por algumas épocas
for epoch in range(n_epochs_qat):
    treinar_uma_epoca(modelo_preparado, ...)

modelo_quantizado = tq.convert(modelo_preparado.eval(), inplace=False)
```

* **Vantagem:** recupera boa parte da precisão perdida pelo PTQ — geralmente o gap final fica em menos de 1% de mAP/accuracy comparado ao FP32
* **Custo:** exige re-treinar (ou fine-tunar) o modelo, não é "só converter"

**Quando usar qual:**

| Cenário | Escolha |
|---|---|
| Prototipagem rápida, deadline curto | PTQ — aceita pequena perda de precisão |
| Modelo vai para produção crítica (ex: segurança industrial, saúde) | QAT — vale o custo extra de re-treino |
| Modelo já é robusto e folgado em accuracy (margem grande sobre o mínimo aceitável) | PTQ provavelmente é suficiente |
| Modelo já está no limite do aceitável em FP32 | QAT é praticamente obrigatório — PTQ pode empurrar para fora do aceitável |

### Pruning (Remoção Estrutural de Pesos)

> Complementar à quantização: em vez de reduzir a precisão numérica de cada peso, **remove pesos/canais inteiros** que contribuem pouco para a saída.

```python
import torch.nn.utils.prune as prune

# Pruning não-estruturado (zera pesos individuais — menos ganho real de velocidade)
prune.l1_unstructured(modelo.conv1, name="weight", amount=0.3)  # remove 30% menores

# Pruning estruturado (remove canais/filtros inteiros — ganho real de velocidade,
# porque reduz de fato o tamanho dos tensores, não só zera valores)
prune.ln_structured(modelo.conv1, name="weight", amount=0.3, n=2, dim=0)
```

**Por que pruning não-estruturado raramente ajuda na prática:** zerar pesos individuais não reduz o tamanho do tensor — hardware comum não tem ganho de velocidade real com matrizes esparsas não estruturadas, só com formatos especiais de hardware/software. **Pruning estruturado** (remover filtros/canais inteiros) é o que de fato acelera inferência em GPU/CPU convencional.

### Benchmark de Latência em Hardware Real (não simulado)

> ⚠️ **Erro comum (que o roadmap original não alertava):** medir latência só na sua própria máquina de desenvolvimento (provavelmente uma GPU desktop) e assumir que vai performar igual no hardware de produção (Raspberry Pi, Jetson, ou até um servidor cloud sem GPU). **Sempre valide no hardware-alvo real.**

```python
# Benchmark completo: comparar FP32 vs FP16 vs INT8 no MESMO hardware-alvo
import time

configs = {
    "FP32 (PyTorch)": model_fp32,
    "FP16 (TensorRT)": model_fp16,
    "INT8 (TensorRT/ONNX)": model_int8,
}

resultados = {}
for nome, modelo in configs.items():
    resultados[nome] = benchmark(modelo, img_teste, n=100)

for nome, r in resultados.items():
    print(f"{nome}: {r['fps']:.1f} FPS | {r['latencia_ms']:.1f}ms | "
          f"mAP no conjunto de validação: {avaliar_map(modelo):.3f}")
```

**O exercício correto não é "qual é mais rápido" — é construir a tabela de trade-off completa:**

| Versão | Tamanho | Latência (hardware-alvo) | mAP@0.5 | Aceitável para o SLA? |
|---|---|---|---|---|
| FP32 | 100% | baseline | 0.870 | Referência |
| FP16 | ~50% | ~2x mais rápido | 0.868 | ✅ se SLA permite |
| INT8 (PTQ) | ~25% | ~3-4x mais rápido | 0.831 | ⚠️ avaliar se a queda é aceitável |
| INT8 (QAT) | ~25% | ~3-4x mais rápido | 0.859 | ✅ geralmente vale o re-treino |

### Co-design Modelo↔Hardware

A prática de mercado correta não é "use o modelo mais preciso possível e depois otimize" — é **"escolha o menor modelo que atende ao SLA de latência, e dentro dessa restrição, maximize precisão"**. Isso inverte a ordem natural de quem vem só do mundo de notebook/Kaggle, onde a meta é sempre "accuracy/mAP mais alto possível" sem restrição de runtime.

**Checklist de decisão real:**
1. Qual é o SLA de latência do produto? (ex: "menos de 100ms por frame")
2. Qual hardware vai rodar em produção? (GPU cloud, CPU cloud, Jetson, Raspberry Pi, smartphone)
3. Dado (1) e (2), qual é o **maior** modelo (n/s/m/l/x do YOLO, por exemplo) que ainda cabe no orçamento de latência?
4. Só então: aplicar quantização/pruning se ainda precisar de margem extra

### Edge: Hardware Específico (expandido)

**Raspberry Pi:** modelo nano (n), exportado em ONNX, idealmente já com PTQ int8 — CPU ARM sem aceleração de GPU é o cenário mais restrito
**NVIDIA Jetson:** TensorRT (.engine) com FP16 como padrão, INT8 com QAT se a margem de mAP for crítica
**Apple Silicon (M1/M2):** CoreML — possui seu próprio pipeline de quantização nativo (Core ML Tools)
**Servidor cloud sem GPU (CPU-only):** ONNX Runtime é geralmente a melhor opção — ganho de 2-5x sobre PyTorch puro em CPU sem custo de GPU

---

## 🔹 BLOCO 9 — ROBUSTEZ E AVALIAÇÃO FORA DE DISTRIBUIÇÃO 🆕 (Adição desta revisão)

> 🔧 **Execução obrigatória** — este bloco existe porque é exatamente o tipo de falha que **não aparece no seu conjunto de validação** e só se manifesta quando o modelo já está em produção. Nenhum bloco do roadmap original testava o modelo fora da distribuição em que foi treinado — e isso é citado consistentemente como uma das causas mais comuns de degradação silenciosa em sistemas de visão real.

### O Problema Central

Seu modelo tira mAP@0.5 = 0.87 no conjunto de validação. Você faz deploy. Três semanas depois, o cliente reclama que o sistema "parou de funcionar bem de noite" ou "erra muito quando a câmera está um pouco fora de foco". **O modelo não mudou — a distribuição dos dados de entrada mudou.** Isso se chama **domain shift** (ou distribution shift), e datasets recentes da área (cobrindo, por exemplo, imagens cruas de sensor em condições de baixa luminosidade) existem justamente porque esse é um problema real e não resolvido na maioria dos pipelines de produção.

### Testando Robustez com Perturbações Sintéticas

> A ideia, inspirada em benchmarks de robustez do tipo "ImageNet-C": aplicar corrupções controladas no seu próprio conjunto de validação e medir quanto a métrica cai. Isso simula, de forma barata, o que vai acontecer quando a câmera de produção não estiver em condição ideal.

```python
import cv2
import numpy as np

def aplicar_corrupcoes(img):
    """Gera variações da mesma imagem simulando condições adversas reais."""
    corrupcoes = {}

    # Blur (desfoque de câmera fora de foco / movimento)
    corrupcoes["blur_leve"] = cv2.GaussianBlur(img, (5, 5), 0)
    corrupcoes["blur_forte"] = cv2.GaussianBlur(img, (15, 15), 0)

    # Ruído (sensor de baixa qualidade, baixa luz)
    ruido = np.random.normal(0, 25, img.shape).astype(np.int16)
    corrupcoes["ruido"] = np.clip(img.astype(np.int16) + ruido, 0, 255).astype(np.uint8)

    # Brilho (variação de iluminação dia/noite)
    corrupcoes["escuro"] = np.clip(img.astype(np.int16) - 80, 0, 255).astype(np.uint8)
    corrupcoes["claro_demais"] = np.clip(img.astype(np.int16) + 80, 0, 255).astype(np.uint8)

    # Compressão JPEG agressiva (câmera de produção real, não imagem "limpa" de dataset)
    _, encoded = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 20])
    corrupcoes["jpeg_baixa_qualidade"] = cv2.imdecode(encoded, cv2.IMREAD_COLOR)

    # Oclusão parcial (objeto parcialmente coberto — comum em cenas reais)
    img_ocluida = img.copy()
    h, w = img.shape[:2]
    cv2.rectangle(img_ocluida, (w//4, h//4), (w//2, h//2), (0, 0, 0), -1)
    corrupcoes["oclusao_parcial"] = img_ocluida

    return corrupcoes
```

```python
# Rodar o modelo em cada versão corrompida e comparar a queda de mAP/confiança
resultados_robustez = {}
for nome_corrupcao, img_corrompida in aplicar_corrupcoes(img_original).items():
    resultado = model(img_corrompida)
    resultados_robustez[nome_corrupcao] = {
        "confianca_media": np.mean([float(b.conf) for b in resultado[0].boxes]) if len(resultado[0].boxes) else 0,
        "num_deteccoes": len(resultado[0].boxes)
    }

# Construir tabela de robustez por tipo de corrupção
for corrupcao, metrica in resultados_robustez.items():
    print(f"{corrupcao}: confiança média = {metrica['confianca_media']:.2f}, "
          f"detecções = {metrica['num_deteccoes']}")
```

### O que fazer quando o modelo é frágil a uma corrupção específica

| Corrupção que mais degrada | Ação recomendada |
|---|---|
| Blur | Adicionar `GaussianBlur` na augmentation de treino (Fase 05, Bloco 5) |
| Ruído / baixa luz | Coletar (ou simular) mais exemplos de treino nessas condições especificamente |
| Variação de brilho | `ColorJitter` mais agressivo no treino, ou normalização adaptativa no pré-processamento |
| Compressão JPEG | Treinar com algumas imagens já comprimidas (simula a degradação real da câmera de produção) |
| Oclusão parcial | Cutout/Random Erasing como augmentation |

### Domain Gap entre Dataset de Treino e Câmera de Produção Real

Mesmo sem corrupção sintética, existe um gap estrutural: seu dataset de treino provavelmente vem de fotos "limpas" (alta resolução, boa iluminação, ângulo favorável), enquanto a câmera de produção real tem resolução menor, compressão de stream de vídeo, lente diferente, e ângulo fixo pouco favorável.

**Checklist antes de declarar o modelo "pronto para produção":**
* [ ] Testei com pelo menos 20-30 imagens **capturadas pela câmera/setup real de produção** (não só do dataset de treino/val)
* [ ] Medi a queda de confiança/mAP nessas imagens reais comparado ao conjunto de validação
* [ ] Testei em pelo menos 2 condições de iluminação diferentes (se aplicável ao caso de uso)
* [ ] Documentei essa queda no README do projeto (conecta com "Limitações Conhecidas" da Fase 12)

### 🎯 Domínio

* Saber que mAP alto no conjunto de validação **não é garantia** de robustez em produção
* Construir o hábito de testar robustez **antes** do deploy, não depois que o cliente reclamar

### 🚧 Mini-projeto

* Pegar o modelo treinado na Fase 07 ou 08
* Aplicar as 6 corrupções do código acima no conjunto de validação completo
* Gerar uma tabela única: corrupção × queda de mAP/confiança
* Identificar a corrupção mais prejudicial e aplicar a mitigação correspondente da tabela acima

---

## 🔹 BLOCO 10 — TESTES AUTOMATIZADOS E CI BÁSICO PARA ML 🆕 (Adição desta revisão)

> 🔧 **Execução obrigatória** — este é o bloco que separa "treinei um modelo" de "sou engenheiro de software que trabalha com ML". É cobrado em praticamente toda entrevista técnica sênior de CV/MLE, e estava completamente ausente do roadmap original.

### Por que testar pré/pós-processamento (não o modelo em si)

Você não escreve um "unit test" que verifica se o modelo prediz corretamente — isso é o papel da avaliação com métricas (mAP, IoU, etc.), já cobertas nas Fases 07/08. O que você **testa com `pytest`** são as partes determinísticas do pipeline: funções de pré-processamento, pós-processamento, conversão de formato, e o contrato da API.

```python
# test_preprocessing.py
import numpy as np
import pytest
from src.preprocessing import normalizar_imagem, pascal_to_yolo

def test_normalizar_imagem_retorna_float32_entre_0_e_1():
    img_fake = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
    resultado = normalizar_imagem(img_fake)

    assert resultado.dtype == np.float32
    assert resultado.min() >= 0.0
    assert resultado.max() <= 1.0
    assert resultado.shape == (224, 224, 3)

def test_pascal_to_yolo_converte_corretamente():
    # Bbox conhecida com resultado calculado manualmente — caso de regressão
    x_center, y_center, w, h = pascal_to_yolo(100, 50, 200, 150, img_w=400, img_h=300)

    assert x_center == pytest.approx(0.375, abs=1e-3)
    assert y_center == pytest.approx(0.333, abs=1e-3)
    assert w == pytest.approx(0.25, abs=1e-3)
    assert h == pytest.approx(0.333, abs=1e-3)

def test_pascal_to_yolo_rejeita_bbox_invalida():
    with pytest.raises(ValueError):
        pascal_to_yolo(200, 50, 100, 150, img_w=400, img_h=300)  # x_max < x_min
```

### Teste de Regressão de Modelo (Contrato de Saída, Não Acurácia)

> A ideia: fixar um pequeno conjunto de imagens de referência e garantir que **a saída do pipeline não muda silenciosamente** entre versões de código — isso pega bugs de refatoração antes que cheguem em produção, independente de re-treinar o modelo.

```python
# test_regressao_modelo.py
import json

def test_saida_modelo_nao_muda_silenciosamente():
    """
    Roda o modelo em um conjunto FIXO de imagens de referência e compara
    com resultados salvos anteriormente (snapshot). Se a saída mudar sem
    uma atualização intencional do snapshot, o teste falha — isso pega
    bugs introduzidos por refatoração de código, não por re-treino.
    """
    imagens_referencia = ["tests/fixtures/img_ref_01.jpg", "tests/fixtures/img_ref_02.jpg"]
    with open("tests/fixtures/snapshot_esperado.json") as f:
        esperado = json.load(f)

    for img_path in imagens_referencia:
        resultado = model(img_path)
        num_deteccoes = len(resultado[0].boxes)
        assert num_deteccoes == esperado[img_path]["num_deteccoes"], (
            f"Número de detecções mudou para {img_path} — "
            f"verifique se foi intencional (re-treino) ou bug (refatoração)"
        )
```

### Testando o Contrato da API (FastAPI do Bloco 1)

```python
# test_api.py
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health_check_retorna_ok():
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json()["status"] == "ok"

def test_detectar_com_imagem_valida_retorna_estrutura_esperada():
    with open("tests/fixtures/img_teste.jpg", "rb") as img:
        resposta = client.post("/detectar", files={"file": img})

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert "deteccoes" in corpo
    assert "total" in corpo
    assert isinstance(corpo["deteccoes"], list)

def test_detectar_com_arquivo_invalido_nao_quebra():
    resposta = client.post("/detectar", files={"file": ("teste.txt", b"nao e imagem", "text/plain")})
    assert resposta.status_code in (400, 422)  # Deve rejeitar com erro claro, não 500
```

### GitHub Actions: CI Básico (lint + teste em cada PR)

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Instalar dependências
        run: pip install -r requirements.txt -r requirements-dev.txt

      - name: Lint
        run: ruff check src/

      - name: Rodar testes
        run: pytest tests/ -v

      - name: Checar formatação
        run: black --check src/
```

**Por que isso importa na prática:** sem isso, um colega de equipe (ou você mesmo, 3 meses depois) pode alterar uma função de pré-processamento, quebrar silenciosamente o pipeline, e só descobrir quando o sistema já está em produção dando resultado errado. CI básico pega isso **antes do merge**.

### 🎯 Domínio

* Diferenciar "testar o modelo" (métricas — Fases 07/08) de "testar o pipeline de software ao redor do modelo" (este bloco)
* Ter pelo menos um teste de regressão que protege contra mudanças silenciosas de comportamento

### 🚧 Mini-projeto

* Escrever testes `pytest` para as funções de pré-processamento e pós-processamento do seu projeto da Fase 07 ou 08
* Criar um snapshot de regressão com 3-5 imagens fixas
* Configurar um workflow simples de GitHub Actions que roda os testes em cada PR

---

## 🧪 PROJETOS OBRIGATÓRIOS

### 1️⃣ API de Visão Completa

* FastAPI + endpoint de detecção
* Upload de imagem → JSON com detecções
* Health check endpoint
* Documentação automática via `/docs`

### 2️⃣ Container Docker

* API encapsulada no container
* `docker-compose.yml` com API + Redis
* Container funciona em outra máquina sem nenhuma instalação

### 3️⃣ Pipeline de Re-treinamento

* Salvar imagens com confiança baixa automaticamente
* Script de re-treino que usa dados novos + dados antigos
* Comparar: modelo antigo vs novo em conjunto de validação fixo

### 4️⃣ Dashboard de Monitoramento

```python
# Simples com Streamlit
import streamlit as st, pandas as pd, json

st.title("Monitor de Modelo de Visão")

logs = [json.loads(l) for l in open("logs.jsonl")]
df = pd.DataFrame(logs)

col1, col2, col3 = st.columns(3)
col1.metric("Requests (24h)", len(df))
col2.metric("Latência Média", f"{df.latencia_ms.mean():.0f}ms")
col3.metric("Confiança Média", f"{df.confianca_media.mean():.2%}")

st.line_chart(df.set_index("timestamp")["confianca_media"])
st.bar_chart(df["classes"].explode().value_counts())
```

### 5️⃣ 🆕 Relatório de Quantização e Robustez (Adição desta revisão)

* Tabela comparando FP32 vs FP16 vs INT8: tamanho do modelo, latência no hardware-alvo, e mAP/accuracy
* Tabela de robustez: queda de confiança/mAP para cada tipo de corrupção sintética testada
* Recomendação final justificada: qual versão (precisão numérica) você recomendaria para produção e por quê

### 6️⃣ 🆕 Suite de Testes com CI (Adição desta revisão)

* Testes `pytest` cobrindo pré-processamento, pós-processamento e endpoints da API
* Pelo menos 1 teste de regressão com snapshot fixo
* Workflow do GitHub Actions rodando lint + testes em cada Pull Request

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. FastAPI: endpoint básico
2. Inferência: carregar modelo e rodar
3. Pipeline completo: receber imagem → rodar → retornar JSON
4. Docker: Dockerfile + build + run
5. Docker Compose: API + Redis
6. Pipeline assíncrono (background tasks)
7. Cloud: deploy em Railway/Fly.io
8. DVC: versionar dataset + modelo
9. Logging estruturado (JSON)
10. Monitoramento de confiança
11. Active Learning: salvar imagens incertas
12. Exportar ONNX + benchmark básico
13. 🆕 Quantização PTQ vs QAT: comparar precisão e velocidade
14. 🆕 Pruning estruturado (opcional, se modelo ainda precisa de margem)
15. 🆕 Benchmark completo no hardware-alvo real (não só na máquina de dev)
16. 🆕 Robustez: testar com corrupções sintéticas (blur, ruído, brilho, JPEG, oclusão)
17. 🆕 Testes automatizados: pré/pós-processamento + regressão + contrato de API
18. 🆕 CI básico no GitHub Actions
19. **Dashboard de monitoramento**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Deploy sem monitoramento (modelo degrada silenciosamente)
* Carregar modelo a cada request (latência absurda)
* Não versionar dataset (impossível reproduzir experimento)
* Commitar modelo .pth no Git (arquivo binário gigante)
* Rodar tudo em um script só (não escalável)
* 🆕 Medir latência só na máquina de desenvolvimento e assumir que vale para o hardware de produção
* 🆕 Aplicar quantização sem comparar a queda de mAP/accuracy contra o FP32 original
* 🆕 Declarar modelo "pronto" sem testar com imagens reais do hardware/ambiente de produção
* 🆕 Não ter nenhum teste automatizado protegendo o pipeline contra mudanças silenciosas

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 10 se:

* [ ] API funcionando com modelo real (não mock)
* [ ] Container Docker roda em outra máquina sem nenhuma instalação
* [ ] Pipeline de re-treinamento implementado e testado
* [ ] Logging captura latência e distribuição de predições
* [ ] Monitoramento detecta degradação de confiança
* [ ] Sistema funciona end-to-end com vídeo ou webcam
* [ ] 🆕 Construiu a tabela de trade-off FP32 vs FP16 vs INT8 (tamanho, latência no hardware-alvo, queda de mAP)
* [ ] 🆕 Testou o modelo com pelo menos 5 tipos de corrupção sintética e documentou onde ele é mais frágil
* [ ] 🆕 Tem testes `pytest` cobrindo pré-processamento, pós-processamento e o contrato da API, rodando em CI

---

## 📌 POSIÇÃO FINAL NA TRILHA ATÉ AQUI

```
Fase 00 → Python
Fase 01 → Matemática
Fase 02 → ML Clássico
Fase 03 → Visão Clássica
Fase 04 → Deep Learning
Fase 05 → CNNs
Fase 06 → Transformers
Fase 07 → Detecção
Fase 08 → Segmentação
✅ Fase 09 → MLOps (nível empresa)
```

**Você agora consegue construir:**
* SaaS de visão computacional
* Sistema de monitoramento por câmera
* Produto com IA embarcada

**Próximas fases:** IA Generativa e Visão 3D — uma nova dimensão.


---
