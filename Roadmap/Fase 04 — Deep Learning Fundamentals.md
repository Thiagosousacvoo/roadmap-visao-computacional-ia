# FASE 04 — DEEP LEARNING FUNDAMENTALS

> **Posição na trilha:** Você vai do ML clássico para redes neurais. A diferença é que agora o modelo aprende as próprias features.
> **Nível:** Intermediário → Avançado
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fases 01 (cálculo, gradiente), 02 (ML clássico) e 03 (NumPy avançado) completas

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Álgebra Linear aplicada

* Produto escalar `w · x`
* Multiplicação matriz × vetor
* Shape: `(batch, features)` — você precisa visualizar mentalmente

### Cálculo aplicado

* Derivada: `x² → 2x`
* Regra da cadeia (intuição clara)
* Gradiente: direção de descida

👉 Sem isso, backpropagation vira mágica pura

### NumPy

* Operações vetorizadas, broadcasting
* Manipulação de arrays: reshape, transpose, indexação

### Python estruturado

* Funções, classes (mínimo de POO)
* Separação de arquivos de projeto

### Pipeline de ML (Fase 02)

* Conceito de X/y, treino/teste, métricas

---

## 🔹 BLOCO 0 — TENSORES (FALTAVA ISSO)

> Antes de qualquer rede neural: entender o que é um tensor e como o PyTorch os gerencia.

### O que é Tensor

| Dimensão | Nome | Exemplo |
|---|---|---|
| 0D | Escalar | `42` |
| 1D | Vetor | `[1, 2, 3]` |
| 2D | Matriz | `[[1,2],[3,4]]` |
| 3D | Tensor | Imagem RGB |
| 4D | Batch de Tensores | Batch de imagens |

**Imagem em tensor:**
```
(batch, canais, altura, largura) = (32, 3, 224, 224)
```

### PyTorch Básico

```python
import torch

# Criação
t = torch.tensor([1.0, 2.0, 3.0])
t = torch.zeros(3, 4)
t = torch.ones(2, 3)
t = torch.randn(5, 5)  # Normal padrão

# Propriedades
t.shape    # torch.Size([5, 5])
t.dtype    # torch.float32
t.device   # cpu ou cuda

# Operações
a + b
torch.matmul(a, b)  # Multiplicação de matrizes

# Conversão NumPy ↔ PyTorch
arr = t.numpy()
t = torch.from_numpy(arr)
```

### GPU

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
t = t.to(device)  # Mover tensor para GPU
```

### 🎯 Domínio

* Tensor = evolução do NumPy com suporte a gradiente automático

### 🚧 Mini-exercício

* Recriar 10 operações NumPy no PyTorch e verificar que os resultados são idênticos

---

## 🔹 BLOCO 1 — PERCEPTRON (BASE TOTAL)

> O perceptron é a unidade fundamental de toda rede neural. Antes de usar PyTorch, você vai implementar à mão.

### Estrutura do Neurônio

```
Entradas: x = [x₁, x₂, ..., xₙ]
Pesos:    w = [w₁, w₂, ..., wₙ]
Bias:     b

Operação:
  z = w · x + b          ← produto escalar + bias
  ŷ = f(z)               ← função de ativação
```

### Por que o Bias?

Sem `b`, o hiperplano de decisão sempre passa pela origem. Com `b`, o modelo tem liberdade para deslocar o hiperplano — muito mais poderoso.

### 🚧 Exercício obrigatório: Perceptron Manual (apenas NumPy)

```python
import numpy as np

class PerceptronManual:
    def __init__(self, n_features, lr=0.01):
        self.w = np.random.randn(n_features) * 0.01
        self.b = 0.0
        self.lr = lr

    def predict(self, X):
        z = X @ self.w + self.b
        return (z >= 0).astype(int)  # Ativação degrau (step)

    def fit(self, X, y, epochs=100):
        for epoch in range(epochs):
            for xi, yi in zip(X, y):
                pred = self.predict(xi)
                erro = yi - pred
                self.w += self.lr * erro * xi
                self.b += self.lr * erro

p = PerceptronManual(n_features=2)
p.fit(X_train, y_train)
```

---

## 🔹 BLOCO 2 — FORWARD PASS E BACKPROPAGATION

> Backprop é o coração de toda rede neural. Você precisa entender o fluxo do gradiente antes de deixar o PyTorch fazer automaticamente.

### Forward Pass (da entrada à previsão)

```
Entrada (X)
    ↓
z₁ = W₁ · X + b₁         (camada 1)
    ↓
a₁ = f(z₁)               (ativação)
    ↓
z₂ = W₂ · a₁ + b₂        (camada 2)
    ↓
ŷ = softmax(z₂)           (saída)
    ↓
Loss = CrossEntropy(ŷ, y)
```

### Função de Custo

**MSE (Regressão)**
```
L = (1/n) Σ (ŷ - y)²
```

**Cross-Entropy (Classificação)**
```
L = -(1/n) Σ y·log(ŷ)
```

### Backpropagation (A Regra da Cadeia na Prática)

```
∂L/∂W₂ = ∂L/∂ŷ · ∂ŷ/∂z₂ · ∂z₂/∂W₂
∂L/∂W₁ = ∂L/∂ŷ · ... · ∂z₁/∂W₁  ← regra da cadeia encadeada
```

**Atualização dos pesos:**
```
W = W - lr * ∂L/∂W
b = b - lr * ∂L/∂b
```

### 🚧 Exercício obrigatório: MLP Manual (2 camadas, NumPy)

Implementar rede de 2 camadas com:
* Forward pass completo
* Cálculo de loss
* Backprop manual (calcular gradientes à mão)
* Loop de treino

---

## 🔹 BLOCO 3 — FUNÇÕES DE ATIVAÇÃO

> Sem ativação, uma rede de 10 camadas lineares é equivalente a 1 camada linear. A não-linearidade é o que dá poder real.

### ReLU (Rectified Linear Unit)

```python
def relu(z):
    return np.maximum(0, z)

# Derivada:
def relu_deriv(z):
    return (z > 0).astype(float)
```

* **Quando usar:** Camadas escondidas (hidden layers) — padrão moderno
* **Problema:** Dying ReLU (neurônio que recebe só valores negativos nunca ativa)

### Sigmoid

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

* **Quando usar:** Saída de classificação **binária**
* **Problema:** Gradiente satura para valores extremos de z (vanishing gradient)

### Tanh

```python
def tanh(z):
    return np.tanh(z)
```

* Saída entre -1 e 1 (centralizada em 0 — melhor que sigmoid para camadas escondidas em alguns casos)

### Softmax

```python
def softmax(z):
    e_z = np.exp(z - np.max(z))  # Subtrai max para estabilidade numérica
    return e_z / e_z.sum()
```

* **Quando usar:** Saída de classificação **multi-classe**
* Converte logits em probabilidades que somam 1

### 🎯 Domínio

| Tarefa | Ativação de saída | Loss |
|---|---|---|
| Classificação binária | Sigmoid | BCE |
| Classificação multi-classe | Softmax | Cross-Entropy |
| Regressão | Linear (sem ativação) | MSE |
| Camadas escondidas | ReLU (padrão) | — |

### 🚧 Exercício

* Implementar cada ativação do zero
* Plotar cada função e sua derivada

---

## 🔹 BLOCO 4 — CONCEITOS CRÍTICOS DE TREINAMENTO

### Overfitting em Redes Neurais

* **Causa:** Rede grande demais para dataset pequeno
* **Sintoma:** `loss_treino` caindo, `loss_validação` subindo (divergência)

### Dropout

```python
# Durante treino: desliga neurônios aleatoriamente com probabilidade p
nn.Dropout(p=0.5)

# Durante inferência: desligado automaticamente com model.eval()
```

* **Por que funciona:** Força a rede a não depender de neurônios específicos → generalização

### Batch Normalization

```python
nn.BatchNorm1d(features)  # Para dados 1D (FC layers)
nn.BatchNorm2d(channels)  # Para imagens (Conv layers)
```

* Normaliza entrada de cada camada por batch
* Acelera treino, reduz sensibilidade ao learning rate

### Learning Rate

* Muito alto: pula sobre o mínimo, oscila ou diverge
* Muito baixo: treino extremamente lento, pode prender em mínimo local
* **Prática:** Começar com `1e-3`, observar curva de loss, ajustar

### Batch Size

* Pequeno (8-32): gradiente mais ruidoso, generaliza melhor, mais lento
* Grande (256-512): gradiente mais estável, treina mais rápido, pode generalizar pior

### Época (Epoch)

* 1 época = 1 passagem completa por todo o dataset

### 🎯 Domínio

* Saber o impacto de cada parâmetro e como ajustar com base na curva de loss

---

## 🔹 BLOCO 5 — PYTORCH NA PRÁTICA

### Estrutura Padrão de Treino

```python
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# 1. Dataset customizado
class MeuDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.FloatTensor(X)
        self.y = torch.LongTensor(y)
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 2. Modelo
class MeuModelo(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.rede = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_size, output_size)
        )
    
    def forward(self, x):
        return self.rede(x)

# 3. Instanciar
dataset = MeuDataset(X_train, y_train)
loader = DataLoader(dataset, batch_size=32, shuffle=True)
modelo = MeuModelo(input_size=784, hidden_size=128, output_size=10)
criterio = nn.CrossEntropyLoss()
otimizador = torch.optim.Adam(modelo.parameters(), lr=1e-3)

# 4. Loop de treino (memorizar esta estrutura)
for epoch in range(n_epochs):
    modelo.train()
    for X_batch, y_batch in loader:
        otimizador.zero_grad()       # ← SEMPRE primeiro
        predicoes = modelo(X_batch)  # ← Forward pass
        loss = criterio(predicoes, y_batch)  # ← Loss
        loss.backward()              # ← Backprop (calcula gradientes)
        otimizador.step()            # ← Atualiza pesos
    
    # Validação
    modelo.eval()
    with torch.no_grad():
        # Calcular métricas de validação
        pass

# 5. Salvar e carregar modelo
torch.save(modelo.state_dict(), "modelo.pth")
modelo.load_state_dict(torch.load("modelo.pth"))
```

### 🎯 Domínio

* Montar loop de treino do zero **sem copiar**
* Entender por que `zero_grad()` vem antes de tudo

---

## 🔹 BLOCO 6 — MONITORAMENTO DE TREINO

### Curvas de Aprendizado

```python
historico = {"treino_loss": [], "val_loss": [], "val_acc": []}

# No loop:
historico["treino_loss"].append(loss.item())

# Plotar:
plt.figure(figsize=(12, 4))
plt.subplot(1,2,1)
plt.plot(historico["treino_loss"], label="Treino")
plt.plot(historico["val_loss"], label="Validação")
plt.legend()
plt.title("Loss")
```

### O que olhar

* **Treino e validação caindo juntas** → OK
* **Treino cai, validação para/sobe** → Overfitting → aumentar dropout, reduzir modelo, mais dados
* **Ambas altas e não caem** → Underfitting → modelo maior, mais épocas, lr maior

### TensorBoard

```python
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("runs/experimento1")
writer.add_scalar("Loss/train", loss, global_step)
```

---

## 🧪 PROJETO FINAL (OBRIGATÓRIO)

### Classificador de Dígitos MNIST

**Estrutura:**

```
projeto_dl/
├── data/           ← Dataset MNIST
├── model.py        ← Definição da arquitetura nn.Module
├── train.py        ← Loop de treino + validação + histórico
├── evaluate.py     ← Métricas, confusion matrix, exemplos errados
├── utils.py        ← Funções de normalização, plot
└── main.py         ← Orquestra tudo
```

**Requisitos:**

1. Implementar MLP (sem CNN ainda) com pelo menos 2 camadas
2. Implementar loop de treino completo (sem tutorial aberto)
3. Plotar curvas de loss treino/validação
4. Visualizar exemplos onde o modelo erra
5. Salvar e carregar modelo treinado
6. Testar com imagem desenhada na mão (do mundo real)
7. Atingir > 97% de accuracy no conjunto de teste

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Tensores PyTorch (criar, operar, shape)
2. GPU (`.to(device)`)
3. Perceptron manual (NumPy)
4. Forward pass manual
5. Função de custo (MSE, Cross-Entropy)
6. Backprop manual (2 camadas)
7. Funções de ativação (implementar + plotar)
8. Conceitos: lr, batch, época, dropout
9. Dataset e DataLoader PyTorch
10. `nn.Module` + `nn.Sequential`
11. Loop de treino completo
12. Curvas de aprendizado
13. **Projeto Final: MNIST**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Pular a implementação manual do perceptron e do backprop
* Copiar loop de treino do tutorial sem entender cada linha
* Não entender shapes — erro número 1 em DL
* Ignorar a curva de loss (treinar às cegas)
* Não salvar modelo treinado

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 05 se:

* [ ] Explica forward e backprop sem consultar nada
* [ ] Implementa perceptron do zero com NumPy
* [ ] Treina modelo completo no PyTorch sem copiar tutorial
* [ ] Ajusta hiperparâmetros (lr, batch, dropout) com justificativa baseada nas curvas
* [ ] Identifica overfitting olhando as curvas de loss
* [ ] Modelo MNIST > 97% accuracy


---
