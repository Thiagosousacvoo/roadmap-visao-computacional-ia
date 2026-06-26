Perfeito — essa fase está **bem posicionada**, mas ainda está **abstrata demais para execução real**.  
Vou transformar em um plano **100% operacional**, adicionando o que falta para não virar “copiar tutorial de PyTorch”.

---

# **⚠️ PRÉ-REQUISITOS NECESSÁRIOS (ANTES DA FASE 4\)**

## **🔹 Fundamentos (OBRIGATÓRIO)**

### **Álgebra Linear aplicada**

* Produto escalar (w · x)  
* Multiplicação matriz × vetor  
* Shape:  
  * (batch, features)

---

### **Cálculo aplicado**

* Derivada:  
  * x² → 2x  
* Regra da cadeia (intuição)  
* Gradiente:  
  * direção de descida

👉 Sem isso, backprop vira mágica

---

## **🔹 Básico**

### **NumPy**

* Operações vetorizadas  
* Broadcasting  
* Manipulação de arrays

---

## **🔹 Intermediário (CRÍTICO)**

### **Python estruturado**

* Funções  
* Classes (mínimo)  
* Separação de arquivos

---

### **Pipeline de ML**

* X / y  
* treino/teste  
* métricas

---

# **🚨 DIAGNÓSTICO DA FASE**

👉 Está correta, MAS:

* Falta:  
  * implementação manual (crítica)  
  * estrutura de treino real  
  * entendimento de tensores

👉 Ajuste:

* inserir:  
  * “mini rede neural do zero” antes de PyTorch

---

# **🧱 FASE 4 — DEEP LEARNING (REFINADA E EXECUTÁVEL)**

---

# **🔹 BLOCO 0 — TENSORES (FALTAVA ISSO)**

## **📚 O que estudar**

### **O que é tensor**

* Escalar (0D)  
* Vetor (1D)  
* Matriz (2D)  
* Tensor (3D+)

---

### **PyTorch básico**

* torch.tensor  
* dtype  
* shape

---

### **Operações**

* soma  
* multiplicação  
* matmul

---

### **GPU (conceito)**

* `.to("cuda")`

---

## **🎯 Domínio**

* Entender:  
  👉 tensor \= evolução do NumPy

---

## **🚧 Mini-exercício**

* Recriar operações do NumPy no PyTorch

---

# **🔹 BLOCO 1 — PERCEPTRON (BASE TOTAL)**

---

## **📚 Estrutura**

### **Entrada (X)**

* vetor de features

---

### **Pesos (W)**

* vetor de parâmetros

---

### **Bias (b)**

---

### **Operação**

* z \= w·x \+ b

---

### **Ativação**

* f(z)

---

## **🎯 Domínio**

* Entender cada variável no cálculo

---

## **🚧 Exercício obrigatório**

* Implementar perceptron manual:  
  * sem PyTorch  
  * só NumPy

---

# **🔹 BLOCO 2 — FORWARD E BACKPROP**

---

## **📚 Forward pass**

### **Etapas**

1. Entrada  
2. Multiplicação  
3. Soma  
4. Ativação  
5. Saída

---

## **📚 Função de custo**

* MSE (início)  
* CrossEntropy (classificação)

---

## **📚 Backpropagation**

### **Conceitos:**

* calcular erro  
* derivar erro  
* atualizar pesos

---

### **Atualização**

* w \= w \- lr \* gradiente

---

## **🎯 Domínio**

* Entender fluxo completo:  
  👉 entrada → erro → ajuste

---

## **🚧 Exercício obrigatório**

* Treinar perceptron manualmente:  
  * ajustar pesos em loop

---

# **🔹 BLOCO 3 — FUNÇÕES DE ATIVAÇÃO**

---

## **📚 ReLU**

* max(0, x)

---

## **📚 Sigmoid**

* saída entre 0 e 1

---

## **📚 Tanh**

* saída entre \-1 e 1

---

## **📚 Softmax**

* distribuição de probabilidade

---

## **🎯 Domínio**

* Saber quando usar:  
  * classificação binária → sigmoid  
  * multi-classe → softmax  
  * hidden layer → ReLU

---

## **🚧 Exercício**

* Implementar funções manualmente

---

# **🔹 BLOCO 4 — CONCEITOS CRÍTICOS**

---

## **📚 Overfitting em redes**

* modelo memoriza

---

## **📚 Dropout**

* desligar neurônios aleatoriamente

---

## **📚 Batch Normalization (conceito)**

* normalizar entrada por batch

---

## **📚 Learning rate**

* tamanho do passo

---

## **📚 Época**

* 1 passagem completa no dataset

---

## **📚 Batch size**

* tamanho do lote

---

## **🎯 Domínio**

* Saber impacto de cada parâmetro

---

# **🔹 BLOCO 5 — PYTORCH NA PRÁTICA**

---

## **📚 Estrutura básica**

### **Dataset**

* torch.utils.data.Dataset

---

### **DataLoader**

* batch  
* shuffle

---

### **Modelo**

* nn.Module  
* forward()

---

### **Loss**

* nn.CrossEntropyLoss

---

### **Otimizador**

* optim.SGD  
* optim.Adam

---

### **Loop de treino**

1. forward  
2. loss  
3. backward  
4. step  
5. zero\_grad

---

## **🎯 Domínio**

* Montar treino do zero SEM copiar

---

## **🚧 Mini-projeto**

* Classificador simples com PyTorch

---

# **🧪 PROJETO FINAL (DETALHADO)**

---

## **🎯 Objetivo**

Classificador de dígitos (MNIST)

---

## **📦 Etapas**

### **1\. Dataset**

* carregar MNIST  
* normalizar dados

---

### **2\. Modelo**

* camada linear  
* ativação ReLU  
* camada de saída

---

### **3\. Treinamento**

* múltiplas épocas  
* batch

---

### **4\. Avaliação**

* accuracy  
* loss

---

### **5\. Ajustes**

* learning rate  
* batch size

---

### **6\. Regularização**

* dropout (opcional)

---

### **7\. Persistência**

* salvar modelo:  
  * torch.save

---

## **📁 Estrutura**

project/

├── data/

├── model.py

├── train.py

├── evaluate.py

├── utils.py

---

# **⏱ ORDEM EXATA**

1. Tensores (PyTorch)  
2. Perceptron (manual)  
3. Forward pass  
4. Função de custo  
5. Backprop (manual)  
6. Ativações  
7. Conceitos (lr, batch, etc.)  
8. PyTorch básico  
9. Loop de treino  
10. MNIST

---

# **⚠️ O QUE EU AJUSTEI**

* Adicionei tensores (faltava totalmente)  
* Forcei implementação manual (crítico)  
* Estruturei treino real (não só teoria)  
* Quebrei PyTorch em partes reais

---

# **🚨 ERROS QUE VOCÊ DEVE EVITAR**

* Pular implementação manual  
* Copiar tutorial de PyTorch  
* Não entender shapes  
* Ignorar loss

---

# **✅ CRITÉRIO REAL DE SAÍDA**

Você só passa se:

* Explica forward e backprop  
* Implementa perceptron manual  
* Treina modelo no PyTorch sem copiar  
* Ajusta hiperparâmetro conscientemente  
* Identifica overfitting

---

