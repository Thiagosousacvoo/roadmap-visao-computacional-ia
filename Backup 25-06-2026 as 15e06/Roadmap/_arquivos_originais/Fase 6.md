Perfeito — essa fase já entra em **nível de produto real**, mas ainda tem pontos críticos faltando (principalmente **dataset, pipeline e engenharia de treino**).

Vou transformar em um plano **totalmente executável \+ nível mercado**.

---

# **⚠️ PRÉ-REQUISITOS NECESSÁRIOS (ANTES DA FASE 6\)**

## **🔹 Fundamentos obrigatórios**

### **CNN (Fase 5 sólida)**

Você precisa:

* Entender:  
  * convolução  
  * feature maps  
  * pooling  
* Treinar CNN do zero  
* Usar PyTorch com segurança

---

## **🔹 Básico**

### **Imagem e vídeo**

* OpenCV:  
  * leitura de imagem  
  * leitura de vídeo  
  * frame a frame

---

## **🔹 Intermediário (CRÍTICO)**

### **Treinamento de modelos**

* Dataset → treino → validação  
* Overfitting  
* Métricas (precision, recall, F1)

---

### **Estrutura de projeto**

* Separação:  
  * data/  
  * train/  
  * inference/

👉 Se isso não estiver sólido, você não consegue escalar projeto

---

# **🚨 DIAGNÓSTICO DA FASE**

👉 Muito boa conceitualmente, MAS faltava:

* Pipeline de dataset (ANOTAÇÃO — CRÍTICO)  
* Formato de dados (YOLO format)  
* Debug de treino  
* Deploy/inferência estruturada

👉 Corrigido abaixo.

---

# **🚀 FASE 6 — OBJECT DETECTION (REFINADA E EXECUTÁVEL)**

---

# **🔹 BLOCO 1 — CONCEITOS FUNDAMENTAIS**

---

## **📦 Bounding Box**

### **Formatos:**

#### **Pascal VOC**

* (x\_min, y\_min, x\_max, y\_max)

---

#### **YOLO (CRÍTICO)**

* (x\_center, y\_center, width, height)  
* valores normalizados (0–1)

---

## **📊 IoU (Intersection over Union)**

* interseção / união

---

## **🎯 mAP**

### **Componentes:**

* Precision  
* Recall  
* IoU threshold

---

## **🎯 Domínio**

* Avaliar modelo corretamente (não só “parece bom”)

---

## **🚧 Exercício**

* Calcular IoU manual com dois boxes

---

# **🔹 BLOCO 2 — PIPELINE DE DETECÇÃO (FALTAVA ISSO)**

---

## **📚 Etapas reais**

1. Coletar imagens  
2. Anotar bounding boxes  
3. Dividir dataset:  
   * train  
   * val  
4. Treinar modelo  
5. Avaliar  
6. Ajustar  
7. Deploy

---

## **🛠 Ferramentas**

* Roboflow  
* LabelImg

---

## **🎯 Domínio**

* Criar dataset do zero

---

# **🔹 BLOCO 3 — COMO FUNCIONA DETECTOR**

---

## **🔹 Two-stage**

### **R-CNN**

### **Faster R-CNN**

* gerar regiões → classificar

---

## **🔹 One-stage**

### **YOLO**

### **SSD**

* detectar direto

---

## **🎯 Domínio**

* Saber escolher:  
  * precisão vs velocidade

---

# **🔹 BLOCO 4 — YOLO (PRÁTICA REAL)**

---

## **📚 Ferramenta**

* Ultralytics YOLO

---

## **📚 Estrutura do dataset (YOLO)**

dataset/  
├── images/  
│   ├── train/  
│   ├── val/  
├── labels/  
│   ├── train/  
│   ├── val/

---

## **📚 Arquivo de label**

Formato:

classe x\_center y\_center width height

---

## **📚 Treinamento**

* epochs  
* batch  
* image size

---

## **📚 Inferência**

* imagem  
* vídeo  
* webcam

---

## **🎯 Domínio**

* Treinar modelo do zero SEM tutorial

---

## **🚧 Mini-projeto BLOCO 4**

* Treinar YOLO com dataset simples

---

# **🔹 BLOCO 5 — PROJETOS OBRIGATÓRIOS (DETALHADO)**

---

## **1️⃣ Webcam (tempo real)**

* detectar pessoas

---

## **2️⃣ Multi-classes**

* ex: pessoa \+ carro

---

## **3️⃣ Dataset próprio (CRÍTICO)**

* ex:  
  * capacete vs sem capacete  
  * cinto de segurança

---

## **4️⃣ Vídeo salvo**

* rodar inferência  
* salvar saída

---

# **🔹 BLOCO 6 — TRACKING**

---

## **📚 Conceito**

* detectar → associar ao longo do tempo

---

## **Algoritmos:**

### **SORT**

* rápido  
* simples

---

### **DeepSORT**

* usa features visuais

---

## **🎯 Domínio**

* identificar mesmo objeto em frames diferentes

---

## **🚧 Mini-projeto**

* contar pessoas em vídeo

---

# **🔹 BLOCO 7 — OTIMIZAÇÃO (NÍVEL PRODUTO)**

---

## **📚 Exportação**

* ONNX:  
  * interoperabilidade  
* TensorRT:  
  * otimização GPU

---

## **📚 Quantização**

* FP32 → INT8  
* reduzir tamanho  
* aumentar velocidade

---

## **📚 Edge**

### **Hardware:**

* Raspberry Pi  
* Jetson Nano

---

## **🎯 Domínio**

* Rodar modelo fora do PC

---

# **🔹 BLOCO 8 — DEBUG E MELHORIA (FALTAVA ISSO)**

---

## **📚 Problemas comuns**

### **Overfitting**

* treino alto, validação baixa

---

### **Underfitting**

* ambos ruins

---

### **Dataset ruim**

* pouca variedade  
* classes desbalanceadas

---

## **📚 Ajustes**

* mais dados  
* augmentation  
* ajustar learning rate

---

## **🎯 Domínio**

* Melhorar modelo com estratégia

---

# **⏱ ORDEM EXATA**

1. Bounding box \+ IoU  
2. mAP  
3. Pipeline de dataset  
4. YOLO formato  
5. Treino YOLO  
6. Inferência  
7. Dataset próprio  
8. Tracking  
9. Otimização  
10. Deploy básico

---

# **⚠️ O QUE EU AJUSTEI**

* Adicionei pipeline de dataset (CRÍTICO)  
* Detalhei formato YOLO  
* Estruturei treino real  
* Adicionei debug de modelo  
* Incluí deploy/edge

---

# **🚨 ERROS QUE VOCÊ DEVE EVITAR**

* Não rotular dataset próprio  
* Usar só modelo pré-treinado  
* Ignorar métricas (mAP)  
* Dataset pequeno e enviesado  
* Não validar resultado

---

# **✅ CRITÉRIO REAL DE SAÍDA**

Você só passa se:

* Treina detector do zero  
* Usa dataset próprio  
* Avalia com mAP  
* Detecta em vídeo em tempo real  
* Consegue melhorar modelo

---

