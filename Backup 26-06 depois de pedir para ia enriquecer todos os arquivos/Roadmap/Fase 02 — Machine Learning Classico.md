# FASE 02 — MACHINE LEARNING CLÁSSICO

> **Posição na trilha:** Primeiro contato com modelos que aprendem. Sem isso, Deep Learning vira caixa-preta.
> **Nível:** Intermediário
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 01 completa

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Álgebra Linear aplicada

* Vetor: soma, norma, dot product
* Matriz: multiplicação, dimensão (shape)
* Autovalores: apenas intuição

### Cálculo (mínimo funcional)

* Derivada de `x²` → `2x`
* Gradiente de função de 2 variáveis
* Regra da cadeia (intuição)

### Python + NumPy + Pandas

* Criar e operar arrays vetorizados (sem `for`)
* DataFrame: filtro, seleção de coluna, limpeza

### Estrutura de Projeto

* Separar arquivos: `data/`, `model/`, `train/`
* Ler CSV e separar X e y

👉 Se isso não estiver sólido, você vai virar "usuário de biblioteca"

---

## 🔹 BLOCO 1 — FUNDAMENTOS DO APRENDIZADO DE MÁQUINA

### 1. O que o modelo faz

* Aprender uma função `f(X) ≈ y` a partir de exemplos
* **Supervisionado:** Temos as respostas certas (y)
* **Não supervisionado:** Não temos respostas → encontrar estrutura nos dados
* **Diferença-chave:** ML clássico = engenharia de features; DL = aprendizado automático de features

> 🆕 **Conectando com a Fase 01:** lá você aprendeu Teorema de Bayes e Entropia como conceitos isolados de probabilidade. Aqui é onde eles voltam como ferramenta prática:
> * **Naive Bayes** (classificador, não coberto em detalhe nesta fase mas vale conhecer o nome) aplica Bayes diretamente: `P(classe|features) ∝ P(features|classe) · P(classe)`, assumindo features independentes.
> * **Entropia** reaparece no Bloco 2 como critério de divisão em Árvores de Decisão, e novamente como base da **Cross-Entropy Loss** usada em quase toda classificação em Deep Learning (Fase 04 em diante).
> * **Calibração de probabilidade:** quando você usa Regressão Logística e a saída é "73% de chance de ser classe positiva", isso só é confiável se o modelo estiver **calibrado** — ou seja, se entre todas as previsões com 73% de confiança, de fato ~73% forem positivas na realidade. Modelos podem ter boa accuracy e ainda assim estarem mal calibrados (confiantes demais ou de menos). Ferramenta prática: `sklearn.calibration.calibration_curve` e `CalibratedClassifierCV`. Isso importa especialmente quando a probabilidade de saída vai ser usada para decisão (ex: "só alertar se confiança > 90%").

### 2. Estrutura do Dataset

**Features (X)**
* Matriz de entrada: formato `(n_samples, n_features)`

**Labels (y)**
* Vetor de saída
* Regressão: valores contínuos (ex: preço de casa)
* Classificação: classes (ex: gato vs cachorro)

### 3. Divisão de Dados

* `train_test_split(X, y, test_size=0.2, random_state=42)`
* Por que `random_state`? Reprodutibilidade
* Nunca tocar no conjunto de teste até o momento final

### 4. Função de Custo (Loss)

**Regressão — MSE (Mean Squared Error)**
* `MSE = (1/n) Σ (ŷ - y)²`
* Penaliza erros grandes mais que pequenos

**Classificação — Log Loss (Cross-Entropy)**
* `L = -(1/n) Σ [y·log(ŷ) + (1-y)·log(1-ŷ)]`
* Penaliza confiança errada

### 5. Overfitting vs Underfitting

* **Overfitting:** Modelo memoriza treino, falha em dados novos
* **Underfitting:** Modelo simples demais, não aprende nada

* **Viés alto** = underfitting (modelo muito simples)
* **Variância alta** = overfitting (modelo muito complexo)

* **Diagnóstico:** Comparar `loss_treino` vs `loss_validação`
  * `loss_treino` << `loss_val` → overfitting
  * Ambos altos → underfitting

### 🚧 Mini-projeto — BLOCO 1

* Carregar dataset real (ex: Boston Housing ou Iris)
* Separar X e y corretamente
* Dividir treino/teste
* Calcular MSE manualmente com NumPy

---

## 🔹 BLOCO 2 — ALGORITMOS (DETALHADO)

### 1. Regressão Linear

**Conceito**
* Equação: `y = wx + b` (1 feature) ou `y = Xw + b` (múltiplas)
* Objetivo: encontrar `w` e `b` que minimizam o MSE

**Implementação manual (OBRIGATÓRIO)**

```python
# Sem sklearn — apenas NumPy
def predict(X, w, b):
    return X @ w + b

def mse(y_pred, y_true):
    return np.mean((y_pred - y_true) ** 2)

# Gradient descent manual
for epoch in range(epochs):
    y_pred = predict(X_train, w, b)
    loss = mse(y_pred, y_train)
    # Calcular gradientes
    dw = -(2/n) * X_train.T @ (y_train - y_pred)
    db = -(2/n) * np.sum(y_train - y_pred)
    # Atualizar pesos
    w -= lr * dw
    b -= lr * db
```

**Com sklearn:**
* `LinearRegression().fit(X_train, y_train)`

**🎯 Domínio:** Entender cada parte do cálculo — não só usar a lib

---

### 2. Regressão Logística

**Conceito**
* Classifica em 2 classes (binário)
* Aplica função sigmoid à saída: `σ(z) = 1 / (1 + e^(-z))`
* Saída = probabilidade, não classe direta

**Por que sigmoid?**
* Transforma qualquer valor real em probabilidade [0, 1]

**Implementação**
* `LogisticRegression()` do sklearn
* Implementar sigmoid manualmente: `1 / (1 + np.exp(-z))`

**🎯 Domínio:** Entender que a saída é probabilidade, não classe

---

### 3. Árvores de Decisão

**Conceito**
* Divide dados com regras `if/else` aprendidas dos dados
* Critério de divisão:
  * Gini: mede impureza
  * Entropia: mede desordem informacional

**Hiperparâmetros críticos**
* `max_depth`: profundidade máxima — controla overfitting
* `min_samples_split`: mínimo de amostras para dividir

**Vantagem:** Interpretável (você consegue ver a árvore)  
**Desvantagem:** Overfita facilmente sem regularização

---

### 4. Random Forest

**Conceito**
* Conjunto de múltiplas árvores de decisão
* Cada árvore treinada em subconjunto aleatório dos dados (bagging)
* Previsão = votação da maioria (classificação) ou média (regressão)

**Por que funciona melhor?**
* A aleatoriedade reduz correlação entre árvores
* Erros de uma árvore são compensados por outras

**Hiperparâmetros**
* `n_estimators`: número de árvores (mais = mais estável, mais lento)
* `max_features`: features a considerar por split

---

### 5. KNN (K-Nearest Neighbors)

**Conceito**
* Classifica ponto novo pela maioria dos K vizinhos mais próximos
* Não "treina" — apenas memoriza o dataset

**Hiperparâmetro crítico**
* `k` pequeno → overfitting; `k` grande → underfitting

**Quando usar:** Datasets pequenos, problema simples

---

### 6. SVM (Support Vector Machine)

**Conceito (intuição)**
* Encontra o hiperplano que maximiza a margem entre classes
* **Kernel trick:** Projeta dados em dimensão superior para separar o que não é linearmente separável

**Quando usar:** Dados de alta dimensão, margem clara entre classes

---

### 7. PCA Revisitado (Aplicação Prática)

**No contexto de ML:**
* Reduzir dimensionalidade antes de treinar modelo
* Remover features altamente correlacionadas
* Acelerar treino e reduzir overfitting

**Com sklearn:**
* `from sklearn.decomposition import PCA`
* `pca = PCA(n_components=2)`
* Plotar dados projetados para visualizar separabilidade

**🎯 Domínio:** Saber quando usar — quando tem muitas features correlacionadas

---

### 🚧 Mini-projeto — BLOCO 2

* Treinar regressão linear + regressão logística
* Comparar resultados com e sem normalização das features
* Visualizar decision boundary da regressão logística

---

## 🔹 BLOCO 3 — AVALIAÇÃO DE MODELO

A escolha da métrica errada é um erro de iniciante que mata projetos.

### 1. Métricas de Classificação

**Accuracy**
* `acertos / total`
* ⚠️ Inútil em datasets desbalanceados (99% gato, 1% cachorro → modelo que chuta "gato" tem 99% accuracy)

**Precision**
* Dos que previ como positivo, quantos eram mesmo positivos?
* `TP / (TP + FP)`
* Importante quando: falso positivo é caro (ex: email legítimo na spam)

**Recall**
* Dos que eram positivos, quantos eu acertei?
* `TP / (TP + FN)`
* Importante quando: falso negativo é caro (ex: câncer não detectado)

**F1-Score**
* Média harmônica de Precision e Recall
* `F1 = 2 * (P * R) / (P + R)`
* Equilíbrio entre os dois

**Confusion Matrix**
* Tabela TP, FP, FN, TN
* Visualizar onde o modelo erra

### 2. Métricas de Regressão

**MSE** (Mean Squared Error) — penaliza erros grandes  
**MAE** (Mean Absolute Error) — mais robusto a outliers  
**R² Score** — quanto da variância o modelo explica (1.0 = perfeito)

### 🛠 Ferramentas

* `sklearn.metrics`: `accuracy_score`, `precision_score`, `recall_score`, `f1_score`, `confusion_matrix`

### 🎯 Domínio

* **Fraude:** usar recall (não deixar fraude passar = falso negativo é fatal)
* **Spam:** usar precision (não marcar email legítimo como spam = falso positivo é fatal)
* **Geral balanceado:** usar F1 ou accuracy

### 🚧 Mini-projeto — BLOCO 3

* Avaliar modelo com todas as métricas
* Plotar confusion matrix com Matplotlib/Seaborn
* Explicar em texto o que cada número na matriz significa

---

## 🔹 BLOCO 4 — AJUSTE E REGULARIZAÇÃO DE MODELO

### 1. Hiperparâmetros vs Parâmetros

* **Parâmetros:** Aprendidos durante treino (ex: pesos `w`)
* **Hiperparâmetros:** Definidos antes do treino (ex: `max_depth`, `learning_rate`)

### 2. Regularização

**L1 (Lasso)**
* Penaliza a soma dos valores absolutos dos pesos
* Efeito: Zera alguns pesos → seleção automática de features

**L2 (Ridge)**
* Penaliza a soma dos quadrados dos pesos
* Efeito: Reduz pesos mas não zera → mais estável

**Quando usar:**
* Muitas features irrelevantes → L1
* Todas features importam um pouco → L2

### 3. Validação Cruzada (K-Fold)

```
Dataset → [Fold1][Fold2][Fold3][Fold4][Fold5]
Rodada 1: treino=[2,3,4,5], teste=[1]
Rodada 2: treino=[1,3,4,5], teste=[2]
...
Score final = média das 5 rodadas
```

* Por que usar: Estimativa mais robusta da performance
* `cross_val_score(model, X, y, cv=5)`

### 4. Grid Search

* Testar combinação de hiperparâmetros sistematicamente
* `GridSearchCV(model, param_grid, cv=5)`
* **Cuidado:** Cresce exponencialmente com número de parâmetros

### 5. Pipeline sklearn

```python
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])
pipeline.fit(X_train, y_train)
```

* **Por que usar:** Evita data leakage — o scaler aprende só no treino

### 🚧 Mini-projeto — BLOCO 4

* Ajustar Random Forest com `GridSearchCV`
* Comparar: sem ajuste vs com ajuste (métricas)
* Usar `Pipeline` com normalização

---

## 🧪 PROJETO FINAL (OBRIGATÓRIO)

### Dataset real (ex: Kaggle Titanic ou Heart Disease)

**Pipeline completo:**

```
projeto_ml/
├── data/
│   ├── raw/
│   └── processed/
├── preprocessing.py   ← limpeza, encoding, normalização
├── train.py           ← treino e validação cruzada
├── evaluate.py        ← métricas, confusion matrix, relatório
├── utils.py           ← funções auxiliares
└── main.py            ← orquestra tudo
```

**Etapas obrigatórias:**

1. Cargar e limpar dados (missing values, tipos, outliers)
2. Feature engineering: criar features derivadas
3. Separar X / y corretamente
4. Pipeline com StandardScaler + modelo
5. Treinar mínimo 3 modelos diferentes
6. Validação cruzada (5-fold) em cada
7. Avaliação com métricas completas
8. Diagnóstico: qual modelo sofre mais overfitting?
9. Ajuste de hiperparâmetros no melhor modelo

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Conceito de aprendizado supervisionado
2. Dataset (X, y), train_test_split
3. MSE manual (NumPy)
4. Regressão linear manual (gradient descent)
5. Regressão linear com sklearn
6. Regressão logística (sigmoid)
7. Árvores de decisão
8. Random Forest
9. KNN e SVM (conceito + uso)
10. PCA (aplicação prática)
11. Métricas completas (precision, recall, F1, confusion matrix)
12. Regularização (L1, L2)
13. Validação cruzada
14. GridSearchCV + Pipeline
15. **Projeto Final**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Usar sklearn sem entender o que acontece dentro
* Não comparar modelos entre si
* Usar só accuracy em dataset desbalanceado
* Não detectar overfitting (comparar treino vs validação)
* Deixar data leakage no preprocessing (scaler vendo dados de teste)
* Pular implementação manual da regressão linear

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 03 se:

* [ ] Treina modelo sem tutorial aberto ao lado
* [ ] Explica o erro do modelo em termos de viés/variância
* [ ] Escolhe métrica correta para o problema
* [ ] Detecta overfitting sozinho olhando as curvas de loss
* [ ] Melhora modelo ajustando hiperparâmetros com justificativa
* [ ] Usa Pipeline para evitar data leakage


---
