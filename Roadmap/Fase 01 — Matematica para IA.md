# FASE 01 — MATEMÁTICA PARA IA

> **Posição na trilha:** Base matemática que sustenta tudo de ML/DL/IA.
> **Nível:** Básico aplicado → Intermediário
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 00 completa

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Aritmética sólida

* Soma, subtração, multiplicação, divisão
* Frações: soma, simplificação
* Potência: `x²`, `x³`
* Raiz quadrada: `√4`, `√9`
* Ordem de operações

👉 **Domínio:** Resolver contas sem travar

---

### Interpretação de funções (CRÍTICO)

* O que é função: entrada → saída
* Notação: `f(x)`, `y = f(x)`
* Avaliação: `f(2) = ?`
* Gráfico (intuição): reta, parábola

👉 **Domínio:** Entender "entrada vira saída" naturalmente

---

### Vetor intuitivo (antes da álgebra formal)

* Vetor como: seta no plano, lista de números
* Soma de vetores (intuição visual)
* Escala: multiplicar vetor por escalar

👉 Se isso não estiver claro, álgebra linear vira decoreba

---

## ⚠️ IMPORTANTE: Estratégia de Aprendizado

Esta fase **não é matemática acadêmica**. É matemática aplicada para código.

**Regra obrigatória:** Cada conceito = implementar em NumPy imediatamente.  
Nunca avance de tópico sem ter rodado o código.

---

## 🔹 BLOCO 1 — VETORES (COMEÇO REAL)

Vetores são a unidade fundamental de dados em IA. Um pixel é um vetor. Uma imagem é uma matriz de vetores. Um embedding de texto é um vetor.

### Representação

* Vetor como lista: `[1, 2]`, `[3, 4, 5]`
* Em NumPy: `np.array([1, 2, 3])`
* Dimensão: `shape` do array

### Operações

* Soma: `[1,2] + [3,4] = [4,6]`
* Subtração
* Multiplicação por escalar: `2 * [1,2] = [2,4]`

### Norma (Magnitude)

* Comprimento do vetor: `‖v‖ = √(x² + y²)`
* Em NumPy: `np.linalg.norm(v)`

### Produto Escalar (Dot Product)

* Soma dos produtos elemento a elemento
* `a · b = a₁b₁ + a₂b₂ + ...`
* Em NumPy: `np.dot(a, b)`
* **Por que importa:** Base de toda multiplicação de pesos em redes neurais

### Similaridade por Cosseno

* `cos(θ) = (a·b) / (‖a‖ * ‖b‖)`
* Valores entre -1 e 1
* **Por que importa:** Mede similaridade entre vetores sem depender da magnitude

### 🛠 Ferramentas NumPy

* `np.array`, `np.linalg.norm`, `np.dot`

### 🎯 Domínio

* Entender vetor como: posição, direção, intensidade

### 🚧 Mini-projeto

* Calcular similaridade por cosseno entre pares de vetores
* Implementar **sem** `sklearn` — só NumPy

---

## 🔹 BLOCO 2 — MATRIZES (BASE REAL DE IA)

Uma imagem é uma matriz. Os pesos de uma rede neural são matrizes. Entender matrizes é entender o que acontece dentro de qualquer modelo.

### Representação

* Matriz como tabela: linhas × colunas
* Em NumPy: array 2D

### Dimensão (CRÍTICO)

* `shape`: `(linhas, colunas)`
* Compatibilidade de operação: regra de tamanho

### Operações

**Multiplicação matriz × vetor**
* Regra: `(m×n) @ (n,) = (m,)`
* Interpretação: aplicar transformação linear ao vetor

**Multiplicação matriz × matriz**
* Regra: `(m×k) @ (k×n) = (m×n)`
* Linha × coluna

**Transposta**
* Inverter linhas/colunas: `A.T`

**Inversa**
* `np.linalg.inv(A)` — quando existe

### Determinante

* Escalar que descreve como a matriz "escala o espaço"
* `np.linalg.det(A)`

### 🛠 Ferramentas NumPy

* `.shape`, `np.dot` / `@`, `.T`, `np.linalg.inv`

### 🎯 Domínio

* Saber quando uma operação é válida ou não pelo shape

### 🚧 Mini-projeto

* Aplicar matriz de transformação em conjunto de pontos 2D
* Visualizar antes/depois com Matplotlib

---

## 🔹 BLOCO 3 — SISTEMAS LINEARES

### Conceito

* Sistema de equações lineares:
  * `2x + y = 5`
  * `x - y = 1`

### Interpretação Geométrica

* Solução = ponto de interseção de retas (2D) ou planos (3D)

### Forma Matricial

* `Ax = b`
* Resolver: `np.linalg.solve(A, b)`

### Quando não há solução

* Sistema inconsistente ou sub-determinado
* Pseudo-inversa: `np.linalg.lstsq`

### 🎯 Domínio

* Entender solução como ponto de interseção
* Saber quando o sistema não tem solução única

---

## 🔹 BLOCO 4 — TRANSFORMAÇÕES LINEARES

### Conceito

* Matriz = transformação (não só "tabela de números")

### Tipos de Transformação

* **Escala:** Esticar/comprimir eixos
* **Rotação:** Girar (matriz de rotação 2D)
* **Reflexão:** Espelhar em eixo
* **Projeção:** Projetar em subespaço (intuição)

### Aplicação em Imagem

* Imagem como matriz de pixels
* Transformação altera posição/intensidade dos pixels
* Base para: warp, homografia, data augmentation

### 🚧 Mini-projeto

* Aplicar rotação 2D a conjunto de pontos
* Visualizar transformação sequencial de 3 matrizes

---

## 🔹 BLOCO 5 — AUTOVALORES E AUTOVETORES

### Conceito

* Vetor que **não muda de direção** quando multiplicado pela matriz
* Equação: `Av = λv`
* `λ` (lambda) = autovalor, `v` = autovetor

### Intuição

* "Direções especiais" da transformação
* Autovetores = eixos naturais da transformação
* Autovalores = quanto a transformação estica nessas direções

### Relação com PCA

* PCA encontra as direções de maior variância nos dados
* Essas direções = autovetores da matriz de covariância
* **Por que importa:** Redução de dimensionalidade sem perda significativa

### 🛠 Ferramenta

* `np.linalg.eig(A)` → retorna `(valores, vetores)`

### 🎯 Domínio

* Entender conceito (não decorar fórmula)

### 🚧 Mini-projeto

* Calcular autovalores e autovetores de matriz 2×2
* Visualizar autovetores sobrepostos à transformação

---

## 🔹 BLOCO 6 — CÁLCULO PARA IA

Em IA, cálculo serve para uma coisa principal: **calcular como o erro muda conforme os pesos mudam** (isso é backpropagation).

### Derivada

* Taxa de variação: inclinação da curva em um ponto
* Derivada de `x²` → `2x`
* Derivada de `x³` → `3x²`
* Derivada de constante → `0`
* **Interpretação:** "Para onde vai a função se eu mexer em `x` um pouquinho?"

### Gradiente

* Generalização da derivada para funções de múltiplas variáveis
* Derivada parcial: `∂f/∂x`, `∂f/∂y`
* **Gradiente = vetor com todas as derivadas parciais**
* Aponta na direção de maior crescimento

### Regra da Cadeia

* Derivar função composta: `f(g(x))`
* `d/dx f(g(x)) = f'(g(x)) · g'(x)`
* **Por que importa:** É o fundamento matemático do backpropagation

### Descida do Gradiente (intuição)

* Atualizar parâmetro: `w = w - lr * ∂L/∂w`
* `lr` = learning rate (tamanho do passo)
* Cada passo nos move na direção que reduz o erro

### 🎯 Domínio

* Entender como o erro "volta" da saída para os pesos da rede neural

### 🚧 Mini-projeto

* Implementar descida do gradiente manual para minimizar `f(x) = x²`
* Plotar convergência a cada iteração

---

## 🔹 BLOCO 7 — PROBABILIDADE E ESTATÍSTICA

Modelos de IA são fundamentalmente probabilísticos. Entender distribuições é entender o que o modelo está realmente fazendo.

### Estatística Descritiva

* Média: `soma / quantidade`
* Variância: dispersão em torno da média — `Var = E[(x - μ)²]`
* Desvio padrão: `σ = √variância`
* Mediana e percentis

### Distribuições

**Distribuição Normal (Gaussiana)**
* Curva em forma de sino
* Definida por `μ` (média) e `σ` (desvio padrão)
* Regra 68-95-99.7%
* **Por que importa:** Pesos de redes neurais são inicializados com distribuição normal

**Distribuição Uniforme**
* Todos os valores igualmente prováveis

**Distribuição de Bernoulli**
* Evento binário: sucesso/fracasso
* Base para classificação binária

### Probabilidade Básica

* Probabilidade condicional: `P(A|B)`
* Teorema de Bayes: `P(A|B) = P(B|A) · P(A) / P(B)`
* **Por que importa:** Base de classifiers probabilísticos e modelos generativos

### Entropia

* Medida de incerteza/informação
* `H(x) = -Σ p(x) log p(x)`
* Entropia baixa = distribuição concentrada
* **Por que importa:** Usado em árvores de decisão e como função de perda (cross-entropy)

### 🎯 Domínio

* Interpretar dados, não só calcular

### 🚧 Mini-projeto

* Analisar distribuição de dataset real (Kaggle simples)
* Plotar histograma, calcular z-score, identificar outliers

---

## 🧪 PROJETO FINAL (OBRIGATÓRIO)

### Objetivo: Implementar PCA do zero

O PCA (Principal Component Analysis) é a síntese desta fase: usa álgebra linear (covariância, autovalores) e estatística (variância) juntos.

**Etapas:**

1. Carregar dataset 2D ou 3D (ex: Iris ou MNIST amostrado)
2. Calcular média e centralizar os dados
3. Calcular matriz de covariância: `C = (X - μ)ᵀ (X - μ) / (n-1)`
4. Calcular autovalores e autovetores de `C`
5. Ordenar por autovalor decrescente
6. Projetar dados nos k primeiros autovetores
7. Visualizar antes e depois da redução

**Regra:** Implementar **sem sklearn.PCA** — apenas NumPy.  
Depois comparar resultado com `sklearn.decomposition.PCA` para validar.

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Vetores (representação, operações, norma, dot product)
2. Similaridade por cosseno
3. Matrizes (dimensão, multiplicação, transposta)
4. Sistemas lineares
5. Transformações lineares (visualização)
6. Autovalores e autovetores
7. Derivadas básicas
8. Gradiente e derivadas parciais
9. Regra da cadeia
10. Descida do gradiente (implementação manual)
11. Probabilidade e distribuições
12. Entropia
13. **Projeto Final: PCA do zero**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Assistir aula e achar que entendeu — **implementar é obrigatório**
* Decorar fórmulas sem entender a intuição geométrica
* Pular para cálculo sem dominar álgebra linear
* Não conectar cada conceito com código NumPy

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 02 se:

* [ ] Entende matriz como transformação (não como "tabela")
* [ ] Consegue explicar o que é gradiente sem fórmula
* [ ] Implementa PCA do zero com NumPy
* [ ] Sabe calcular similaridade entre vetores
* [ ] Entende o que é entropia e onde ela aparece em ML
* [ ] Não depende de fórmula decorada — entende de onde ela vem


---
