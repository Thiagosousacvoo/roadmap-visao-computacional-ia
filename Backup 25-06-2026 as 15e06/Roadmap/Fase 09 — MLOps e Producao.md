# FASE 09 — MLOPS E PRODUÇÃO

> **Posição na trilha:** Transforma modelo em produto real. Aqui o modelo sai do notebook e entra no mundo.
> **Nível:** Profissional (engenharia de sistemas)
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
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
12. Exportar ONNX + benchmark
13. **Dashboard de monitoramento**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Deploy sem monitoramento (modelo degrada silenciosamente)
* Carregar modelo a cada request (latência absurda)
* Não versionar dataset (impossível reproduzir experimento)
* Commitar modelo .pth no Git (arquivo binário gigante)
* Rodar tudo em um script só (não escalável)

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 10 se:

* [ ] API funcionando com modelo real (não mock)
* [ ] Container Docker roda em outra máquina sem nenhuma instalação
* [ ] Pipeline de re-treinamento implementado e testado
* [ ] Logging captura latência e distribuição de predições
* [ ] Monitoramento detecta degradação de confiança
* [ ] Sistema funciona end-to-end com vídeo ou webcam

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
