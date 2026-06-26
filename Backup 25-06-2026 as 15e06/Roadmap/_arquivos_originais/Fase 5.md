Perfeito — essa fase está **bem posicionada (nível profissional real)**, mas ainda precisa de **mais granularidade \+ engenharia prática \+ clareza operacional**.

Vou transformar em um plano **sem lacunas**, com execução direta.

---

# **⚠️ PRÉ-REQUISITOS NECESSÁRIOS (ANTES DA FASE 5\)**

## **🔹 Fundamentos obrigatórios**

### **Deep Learning (Fase 4 sólida)**

Você precisa:

* Entender:  
  * forward pass  
  * backpropagation  
* Saber:  
  * o que é tensor  
  * como funciona `nn.Module`  
* Treinar:  
  * modelo simples no PyTorch

👉 Se você ainda copia código → NÃO avance

---

## **🔹 Básico**

### **Imagem como matriz (Fase 3\)**

* RGB \= (H, W, C)  
* Manipular imagem com NumPy/OpenCV

---

## **🔹 Intermediário**

### **PyTorch prático**

* Dataset \+ DataLoader  
* Loop de treino  
* Loss \+ Optimizer

👉 Sem isso, CNN vira tutorial

---

# **🚨 DIAGNÓSTICO DA FASE**

👉 Muito boa, MAS:

* Faltava:  
  * detalhamento da camada Conv2D  
  * controle de shape (CRÍTICO)  
  * debug de modelo  
  * pipeline real de treino

👉 Ajuste feito abaixo.

---

# **🚀 FASE 5 — CNN (REFINADA E EXECUTÁVEL)**

---

# **🔹 BLOCO 1 — CONVOLUÇÃO (NÍVEL ENGENHEIRO)**

---

## **📚 Estrutura da convolução**

### **Kernel**

* tamanho:  
  * 3x3 (principal)  
  * 5x5 (menos comum)

---

### **Operação**

Para cada posição:

1. recorte da imagem  
2. multiplicação elemento a elemento  
3. soma

---

### **Stride**

* passo do kernel:  
  * stride \= 1 (padrão)  
  * stride \= 2 (reduz dimensão)

---

### **Padding**

* adicionar borda:  
  * "same" → mantém tamanho  
  * "valid" → reduz tamanho

---

## **📚 Shape (CRÍTICO)**

### **Entrada:**

* (C, H, W)

### **Saída:**

* depende de:  
  * kernel  
  * stride  
  * padding

---

## **🎯 Domínio**

* Conseguir prever shape da saída SEM rodar código

---

## **🚧 Exercício obrigatório**

* Simular convolução manual com NumPy (revisão)  
* Calcular tamanho da saída manualmente

---

# **🔹 BLOCO 2 — CAMADA CONVOLUCIONAL (PYTORCH)**

---

## **📚 nn.Conv2d**

### **Parâmetros:**

* in\_channels  
* out\_channels  
* kernel\_size  
* stride  
* padding

---

## **📚 Fluxo interno**

* múltiplos filtros → múltiplos feature maps

---

## **🎯 Domínio**

* Entender:  
  👉 cada filtro aprende padrão diferente

---

## **🚧 Exercício**

* Criar camada Conv2d simples e visualizar saída

---

# **🔹 BLOCO 3 — ARQUITETURA CNN**

---

## **📚 Pipeline completo**

1. Conv2D  
2. ReLU  
3. Pooling  
4. Repetir  
5. Flatten  
6. Linear  
7. Output

---

## **📚 Pooling**

### **Tipos:**

* MaxPooling (principal)  
* AveragePooling

---

### **Função:**

* reduzir dimensão  
* manter informação relevante

---

## **📚 Flatten**

* transformar 3D → 1D

---

## **🎯 Domínio**

* Entender fluxo completo da imagem até saída

---

## **🚧 Exercício**

* Desenhar arquitetura manualmente antes de codar

---

# **🔹 BLOCO 4 — PRIMEIRA CNN (MNIST → CIFAR-10)**

---

## **📚 MNIST (inicial)**

### **Passos:**

* carregar dataset  
* normalizar:  
  * dividir por 255  
* criar CNN simples:  
  * Conv → ReLU → Pool → Linear

---

## **📚 CIFAR-10**

### **Diferença:**

* 3 canais (RGB)  
* mais complexo

---

## **🎯 Domínio**

* Ajustar modelo conforme dataset

---

## **🚧 Mini-projeto**

* Treinar CNN MNIST  
* Evoluir para CIFAR-10

---

# **🔹 BLOCO 5 — DATA AUGMENTATION**

---

## **📚 Transformações**

* RandomHorizontalFlip  
* RandomRotation  
* RandomCrop  
* Normalize

---

## **🛠 Ferramenta**

* torchvision.transforms

---

## **🎯 Domínio**

* Melhorar generalização do modelo

---

## **🚧 Exercício**

* Treinar modelo com e sem augmentation  
* comparar resultado

---

# **🔹 BLOCO 6 — ARQUITETURAS CLÁSSICAS**

---

## **📚 O que estudar (EXATO)**

### **LeNet**

* CNN simples  
* base de tudo

---

### **AlexNet**

* deep CNN  
* uso de ReLU

---

### **VGG**

* camadas profundas com kernels pequenos

---

### **ResNet**

#### **Residual Connection**

* skip connection:  
  * saída \= entrada \+ transformação

---

## **🎯 Domínio**

* Entender evolução das CNNs

---

# **🔹 BLOCO 7 — TRANSFER LEARNING (MUNDO REAL)**

---

## **📚 Conceitos**

### **Modelo pré-treinado**

* já treinado em dataset grande

---

### **Congelar camadas**

* não atualizar pesos

---

### **Fine-tuning**

* ajustar últimas camadas

---

## **🛠 Ferramenta**

* torchvision.models

---

## **🎯 Domínio**

* Usar modelo pronto corretamente

---

## **🚧 Projetos**

### **1\. Gato vs cachorro**

* dataset simples

---

### **2\. Dataset próprio**

* imagens reais

---

# **🔹 BLOCO 8 — VISION TRANSFORMERS (ViT)**

---

## **📚 Conceitos**

### **Patch embedding**

* dividir imagem em blocos

---

### **Self-attention**

* relação entre regiões da imagem

---

### **Position encoding**

* manter ordem espacial

---

## **🎯 Domínio**

* Entender diferença:  
  👉 CNN (local)  
  👉 ViT (global)

---

# **🧪 PROJETOS OBRIGATÓRIOS (DETALHADO)**

---

## **1️⃣ CNN do zero (MNIST)**

* arquitetura simples  
* treino completo

---

## **2️⃣ CNN CIFAR-10**

* RGB  
* maior complexidade

---

## **3️⃣ Transfer Learning com ResNet**

* congelar camadas  
* treinar topo

---

## **4️⃣ Projeto real**

* dataset próprio  
* problema definido

---

# **⏱ ORDEM EXATA**

1. Convolução (teoria \+ prática)  
2. Conv2d (PyTorch)  
3. Pooling  
4. Arquitetura CNN  
5. MNIST  
6. CIFAR-10  
7. Data augmentation  
8. Arquiteturas clássicas  
9. Transfer learning  
10. ViT

---

# **⚠️ O QUE EU AJUSTEI**

* Adicionei controle de shape (CRÍTICO)  
* Detalhei Conv2D real  
* Estruturei pipeline de treino  
* Tornei augmentation comparativo (aprendizado real)  
* Corrigi ViT como visão moderna (não só extra)

---

# **🚨 ERROS QUE VOCÊ DEVE EVITAR**

* Não entender shape → erro nº1  
* Copiar arquitetura pronta  
* Ignorar overfitting  
* Não usar augmentation  
* Pular transfer learning

---

# **✅ CRITÉRIO REAL DE SAÍDA**

Você só passa se:

* Constrói CNN do zero  
* Explica cada camada  
* Ajusta modelo sozinho  
* Usa transfer learning corretamente  
* Resolve problema real com imagens

---

