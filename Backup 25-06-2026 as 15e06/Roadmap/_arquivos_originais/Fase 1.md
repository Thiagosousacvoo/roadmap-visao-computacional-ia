**⚠️ VALIDAÇÃO DE PRÉ-REQUISITOS (ANTES DA FASE 1\)**

Essa fase é **matemática aplicada \+ abstração**.  
Se faltar base, você não entende — só memoriza.

---

## **🔹 Fundamentos (OBRIGATÓRIO)**

### **Aritmética sólida**

* Soma, subtração, multiplicação, divisão  
* Frações:  
  * soma de frações  
  * simplificação  
* Potência:  
  * (2^3), (x^2)  
* Raiz:  
  * √4, √9  
* Ordem de operações (prioridade)

👉 Domínio:

* Resolver contas sem travar

---

### **Interpretação de funções (CRÍTICO)**

* O que é função:  
  → entrada → saída  
* Notação:  
  * f(x)  
  * y \= f(x)  
* Avaliação:  
  * f(2) \= ?  
* Gráfico (intuição):  
  * reta  
  * parábola

👉 Domínio:

* Entender “entrada vira saída” naturalmente

---

## **🔹 Básico**

### **Geometria básica**

* Plano cartesiano (x, y)  
* Distância entre pontos (intuição)  
* Direção e magnitude

---

## **🔹 Intermediário (IMPORTANTE)**

### **Vetor intuitivo (antes da álgebra formal)**

* Vetor como:  
  * seta no plano  
  * lista de números  
* Soma de vetores (intuição)  
* Escala (multiplicar vetor)

👉 Se isso não estiver claro, **álgebra linear vira decoreba**

---

# **🚨 DIAGNÓSTICO DA SUA FASE**

👉 **Está bem estruturada, MAS:**

* Muito **correta conceitualmente**  
* Levemente **densa demais no início (Álgebra Linear pesada logo de cara)**

👉 Ajuste ideal:

* Começar com **vetor → matriz → só depois autovalor**  
* Trazer **NumPy junto desde o início**

---

# **🧱 FASE 1 — MATEMÁTICA PARA IA (REFINADA E EXECUTÁVEL)**

---

# **🔹 BLOCO 1 — VETORES (COMEÇO REAL)**

## **📚 O que estudar (EXATO)**

### **Representação**

* Vetor como lista:  
  * \[1, 2\]  
  * \[3, 4, 5\]

---

### **Operações**

* Soma:  
  * \[1,2\] \+ \[3,4\]  
* Subtração  
* Multiplicação por escalar:  
  * 2 \* \[1,2\]

---

### **Norma (magnitude)**

* Comprimento do vetor

---

### **Produto escalar (dot product)**

* Soma dos produtos

---

## **🛠 Ferramenta**

* NumPy:  
  * np.array  
  * np.linalg.norm  
  * np.dot

---

## **🎯 Domínio**

* Entender vetor como:  
  * posição  
  * direção  
  * intensidade

---

## **🚧 Mini-projeto**

* Calcular similaridade entre vetores

---

# **🔹 BLOCO 2 — MATRIZES (BASE REAL DE IA)**

## **📚 O que estudar**

### **Representação**

* Matriz como:  
  * tabela  
  * array 2D

---

### **Dimensão (CRÍTICO)**

* linhas x colunas  
* compatibilidade de operação

---

### **Operações**

#### **Multiplicação matriz × vetor**

* regra de compatibilidade

#### **Multiplicação matriz × matriz**

* linha × coluna

---

### **Transposta**

* inverter linhas/colunas

---

## **🛠 Ferramenta**

* NumPy:  
  * shape  
  * dot  
  * T

---

## **🎯 Domínio**

* Saber quando operação é válida ou não

---

## **🚧 Mini-projeto**

* Aplicar matriz em vetor (transformação)

---

# **🔹 BLOCO 3 — SISTEMAS LINEARES**

## **📚 O que estudar**

* Sistema de equações:  
  * 2x \+ y \= 5  
  * x \- y \= 1

---

### **Interpretação**

* Interseção de retas

---

### **Forma matricial**

* Ax \= b

---

## **🛠 Ferramenta**

* np.linalg.solve

---

## **🎯 Domínio**

* Entender solução como ponto de interseção

---

# **🔹 BLOCO 4 — TRANSFORMAÇÕES LINEARES**

## **📚 O que estudar**

* Transformar vetor usando matriz

---

### **Tipos**

* escala  
* rotação (intuição)  
* projeção (intuição)

---

### **Aplicação em imagem**

* imagem como matriz  
* transformação altera pixels

---

## **🎯 Domínio**

* Entender que:  
  👉 matriz \= transformação

---

## **🚧 Mini-projeto**

* Aplicar transformação simples em pontos 2D

---

# **🔹 BLOCO 5 — AUTOVALORES E AUTOVETORES**

## **📚 O que estudar**

### **Conceito**

* vetor que não muda direção

---

### **Equação**

* Av \= λv

---

### **Intuição**

* “direções especiais”

---

### **Relação com PCA**

* redução de dimensionalidade

---

## **🛠 Ferramenta**

* np.linalg.eig

---

## **🎯 Domínio**

* Entender conceito (não decorar fórmula)

---

## **🚧 Mini-projeto**

* Calcular autovalores de matriz simples

---

# **🔹 BLOCO 6 — CÁLCULO PARA IA**

---

## **📚 Derivada**

### **O que estudar**

* taxa de variação  
* inclinação da curva

---

### **Prática**

* derivada de:  
  * x²  
  * x³  
  * constante

---

## **📚 Gradiente**

* derivada parcial:  
  * ∂/∂x  
  * ∂/∂y

---

## **📚 Regra da cadeia**

* composição de funções:  
  * f(g(x))

---

## **🎯 Domínio**

* entender:  
  👉 como erro “volta” na rede neural

---

## **🚧 Mini-projeto**

* derivar função simples manualmente

---

# **🔹 BLOCO 7 — PROBABILIDADE**

## **📚 O que estudar**

### **Média**

* soma / quantidade

---

### **Variância**

* dispersão

---

### **Desvio padrão**

* raiz da variância

---

### **Distribuição normal**

* curva gaussiana

---

### **Entropia (intuição)**

* nível de incerteza

---

## **🎯 Domínio**

* interpretar dados, não só calcular

---

## **🚧 Mini-projeto**

* analisar distribuição de dataset

---

# **🧪 PROJETO FINAL (OBRIGATÓRIO)**

## **Você deve implementar:**

### **1\. Álgebra Linear**

* multiplicação de matriz manual (com NumPy e sem)

---

### **2\. Cálculo**

* derivada simples manual  
* gradiente de função simples

---

### **3\. PCA (SIMPLIFICADO)**

* calcular média  
* centralizar dados  
* usar covariância  
* autovalores

---

# **⏱ ORDEM EXATA DE EXECUÇÃO**

1. Vetores  
2. Matrizes  
3. Sistemas lineares  
4. Transformações  
5. Autovalores  
6. Derivadas  
7. Gradiente  
8. Regra da cadeia  
9. Probabilidade

---

# **⚠️ AJUSTES QUE EU FIZ**

* Quebrei álgebra linear em progressão real  
* Integrei NumPy desde o início  
* Separei intuição → operação → aplicação  
* Evitei matemática acadêmica desnecessária  
* Adicionei mini-projetos por bloco

---

# **🚨 ERRO QUE VOCÊ PRECISA EVITAR**

* Assistir aula e achar que entendeu  
* Não implementar  
* Não conectar com código

👉 Regra:  
**cada conceito \= implementar imediatamente**

---

# **✅ CRITÉRIO REAL DE SAÍDA**

Você passou se:

* Entende matriz como transformação  
* Consegue explicar gradiente  
* Implementa PCA básico  
* Não depende de fórmula decorada

---

