# 📚 ROADMAP UNIFICADO: ESPECIALISTA EM VISÃO COMPUTACIONAL E IA
> *Este documento consolida o Índice e todas as 13 Fases da trilha em um único arquivo de referência rápida.*

---

# 🗺️ ROADMAP COMPLETO — ESPECIALISTA EM VISÃO COMPUTACIONAL E IA

> Trilha de 3–5 meses para nível profissional com dedicação intensiva
> Dedicação: mínimo 8h por dia (podendo chegar a 12h)

---

## 📋 ÍNDICE DAS FASES

| Fase | Título | Nível | Tempo Est. (8–12h/dia) |
|---|---|---|---|
| [00](./Fase%2000%20—%20Fundamentos%20Python.md) | Fundamentos Python | Iniciante | 1–2 sem |
| [01](./Fase%2001%20—%20Matematica%20para%20IA.md) | Matemática para IA | Básico aplicado | 1–2 sem |
| [02](./Fase%2002%20—%20Machine%20Learning%20Classico.md) | Machine Learning Clássico | Intermediário | 1–2 sem |
| [03](./Fase%2003%20—%20Visao%20Computacional%20Classica.md) | Visão Computacional Clássica | Intermediário | 1 sem |
| [04](./Fase%2004%20—%20Deep%20Learning%20Fundamentals.md) | Deep Learning Fundamentals | Intermediário-Avançado | 1–2 sem |
| [05](./Fase%2005%20—%20CNNs%20e%20Transfer%20Learning.md) | CNNs e Transfer Learning | Avançado | 1–2 sem |
| [06](./Fase%2006%20—%20NLP%20e%20Transformers.md) | NLP & Transformers ⭐ NOVA | Avançado | 1–2 sem |
| [07](./Fase%2007%20—%20Object%20Detection.md) | Object Detection | Avançado | 1–2 sem |
| [08](./Fase%2008%20—%20Segmentacao.md) | Segmentação | Avançado | 1–2 sem |
| [09](./Fase%2009%20—%20MLOps%20e%20Producao.md) | MLOps e Produção | Profissional | 1–2 sem |
| [10](./Fase%2010%20—%20IA%20Generativa%202D.md) | IA Generativa 2D ⭐ NOVA | Estado da Arte | 2–3 sem |
| [11](./Fase%2011%20—%20Visao%203D%20e%20Neural%20Rendering.md) | Visão 3D e Neural Rendering ⭐ NOVA | Estado da Arte | 2–3 sem |
| [12](./Fase%2012%20—%20Portfolio%20e%20Carreira.md) | Portfólio e Carreira ⭐ NOVA | Profissional | Paralelo |

---

## 🗂️ ESTRUTURA DA TRILHA

```
FUNDAMENTOS (Fases 00-02)
├── Fase 00 — Python: tipos, POO, NumPy, Pandas, ambiente
├── Fase 01 — Matemática: álgebra linear, cálculo, probabilidade
└── Fase 02 — ML Clássico: regressão, árvores, métricas, regularização

VISÃO + DEEP LEARNING (Fases 03-05)
├── Fase 03 — Visão Clássica: OpenCV, convolução manual, vídeo
├── Fase 04 — Deep Learning: perceptron, backprop, PyTorch
└── Fase 05 — CNNs: arquiteturas, transfer learning, ViT (introdução)

MODELO MODERNO (Fase 06) ⭐
└── Fase 06 — Transformers: atenção, ViT completo, CLIP, HuggingFace

DETECÇÃO E SEGMENTAÇÃO (Fases 07-08)
├── Fase 07 — Object Detection: YOLO, tracking, mAP, dataset próprio
└── Fase 08 — Segmentação: U-Net, Mask R-CNN, IoU, pós-processamento

PRODUÇÃO (Fase 09)
└── Fase 09 — MLOps: FastAPI, Docker, monitoramento, active learning

FRONTEIRA (Fases 10-11) ⭐ SPLIT
├── Fase 10 — Generativa 2D: VAE, GAN, Diffusion, LoRA fine-tuning
└── Fase 11 — Visão 3D: câmeras, NeRF, Gaussian Splatting, COLMAP

CARREIRA (Fase 12) ⭐
└── Fase 12 — Portfólio: projetos, GitHub, LinkedIn, entrevistas
```

---

## 🔗 DEPENDÊNCIAS ENTRE FASES

```
00 ──→ 01 ──→ 02 ──→ 03 ──→ 04 ──→ 05 ──→ 06 ──→ 07 ──→ 08 ──→ 09
                              ↓                              ↓
                              └──────── 04 ────────→ 10 ────┘
                                        ↓           ↓
                                       05 ──→ 11 ←──┘
                         
Fase 12 corre em paralelo a partir da Fase 07
```

---

## ⭐ O QUE FOI MUDADO NA NOVA VERSÃO

### Fases Novas

| Fase | Motivo |
|---|---|
| **Fase 06 — NLP & Transformers** | Ponte obrigatória: ViT, CLIP, Stable Diffusion, cross-attention dependem disso |
| **Fase 10 — IA Generativa 2D** | Split da Fase 9 original (era grande demais para 1 fase) |
| **Fase 11 — Visão 3D** | Split da Fase 9 original (duas carreiras distintas: Generativo vs 3D/SLAM) |
| **Fase 12 — Portfólio** | Formaliza o que era nota de rodapé — sem portfólio, a trilha não tem impacto |

### Problemas Corrigidos

| Problema original | Correção |
|---|---|
| Fase 9 era 3–4 especializações de mestrado em 1 fase | Dividida em Fase 10 (2D) e Fase 11 (3D) |
| Stable Diffusion dependia de CLIP nunca ensinado | Fase 06 ensina CLIP antes |
| Fase 8 (MLOps) misturava conceito e execução sem marcar | Blocos marcados como 🔧 execução ou 📖 conceito |
| Fase 7 (Segmentação) tinha Mask R-CNN no mesmo nível da U-Net | Hierarquia ajustada: U-Net primeiro, Mask R-CNN depois |
| Fase 6 (Detection) não referenciava Fase 3 Bloco 4 (vídeo) | Pré-requisito explicitado |
| Sem fase de portfólio/carreira | Fase 12 criada |
| Artefatos de chat nos arquivos ("Perfeito —", "Vou deixar isso...") | Todos removidos |

### Melhorias de Conteúdo

| Fase | O que foi adicionado |
|---|---|
| 00 | Logging, decorator, type hints com exemplos reais |
| 01 | Similaridade por cosseno, implementação da descida do gradiente manual |
| 02 | KNN, SVM, Pipeline sklearn, data leakage explicitado |
| 03 | Armadilha BGR/RGB, pipeline de normalização para DL |
| 04 | Tabela ativação por tarefa, curvas de aprendizado, TensorBoard |
| 05 | Tabela de shapes de convolução, bloco residual com código |
| 07 | Código completo IoU, NMS, tabela diagnóstico de modelo |
| 08 | U-Net implementada em PyTorch, tabela quando usar U-Net vs Mask R-CNN |
| 09 | Blocos marcados conceito vs execução, dashboard Streamlit |
| 10 | DCGAN com boas práticas de estabilização, LoRA fine-tuning |
| 11 | Matemática de câmera com código Python completo |

---

## 📌 NOTAS DE USO

* **Critérios de saída são obrigatórios** — não avance sem cumprir
* **Implementação manual antes da biblioteca** é pedagógico, não tortura
* **Fases 10 e 11** são trilhas de especialização independentes — você pode escolher uma delas com mais profundidade dependendo da carreira
* **Fase 12** começa na Fase 07, não no final

---

*Última atualização: Junho 2026*


---

# FASE 00 — FUNDAMENTOS DE PYTHON

> **Posição na trilha:** Ponto de partida absoluto. Tudo que vem depois depende disso.
> **Nível:** Iniciante → Intermediário
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Lógica de Programação (mínimo funcional)

* O que é algoritmo e sequência de execução
* Estruturas de decisão: `if`, `if/else`, `if/elif/else`
* Estruturas de repetição: `while` e `for` (conceitual)
* Variáveis: criação, atribuição, reatribuição
* Resolução de problemas: transformar problema em passos / pseudo-código

👉 **Domínio:** Resolver problemas simples sem copiar código

---

### Matemática Básica Aplicada

* Operações: `+`, `-`, `*`, `/`
* Ordem de operações (prioridade)
* Porcentagem: calcular `%`, aplicar desconto
* Média: soma / quantidade
* Noção de vetor: lista de números com índice

---

### Ambiente Mínimo

* Instalar Python (`python --version`)
* Executar script: `python arquivo.py`
* Terminal (CLI): `cd`, `ls`/`dir`, criar arquivos e pastas
* Caminho relativo vs absoluto

---

## 🔹 BLOCO 1 — FUNDAMENTOS PYTHON

### 1. Tipos de Dados

**Inteiros (`int`)**
* Operações: `+`, `-`, `*`, `//`, `%`
* Comparação: `==`, `!=`, `<`, `>`, `<=`, `>=`

**Float**
* Precisão de ponto flutuante
* Arredondamento: `round()`

**String**
* Criação: `''`, `""`
* Concatenação, repetição
* Indexação e slicing: `[inicio:fim]`, `[::passo]`
* Métodos: `lower()`, `upper()`, `strip()`, `replace()`, `split()`, `join()`

**Boolean**
* `True` / `False`
* Operadores: `and`, `or`, `not`

**Conversão de tipos**
* `int()`, `float()`, `str()`

---

### 2. Estruturas de Dados

**Listas**
* Criação `[]`, acesso por índice, slicing
* Métodos: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`
* Listas aninhadas

**Tuplas**
* Criação `()`, imutabilidade, unpacking

**Sets**
* Criação `set()`, remoção de duplicados
* Operações: união `|`, interseção `&`

**Dicionários**
* Criação `{}`, chave → valor
* Acesso: `dict["chave"]`
* Métodos: `keys()`, `values()`, `items()`, `get()`

---

### 3. Condições e Loops

**Condições**
* `if`, `elif`, `else`
* Operadores relacionais e lógicos

**Loops**
* `for` → iterar lista, string, range
* `while` → condição de parada
* Controle: `break`, `continue`

**List Comprehension**
* Sintaxe básica: `[expr for x in lista]`
* Com condição: `[expr for x in lista if cond]`
* Aninhado (nível básico)

---

### 4. Funções

* `def`, parâmetros obrigatórios e opcionais (default)
* `return` simples e múltiplos valores
* Escopo: local vs global
* Funções dentro de funções (closures básico)

---

### 5. Exceções

* `try`, `except`, `except ValueError/TypeError`
* `else`, `finally`

---

### 6. Arquivos

**Leitura**
* `open()`, `read()`, `readline()`, `readlines()`

**Escrita**
* `write()`, modo append

**CSV sem pandas**
* Separar por vírgula, `split()`

---

### 🎯 Mini Projeto — BLOCO 1

* Ler CSV manualmente (sem pandas)
* Filtrar linhas com condição
* Salvar novo CSV filtrado

---

## 🔹 BLOCO 2 — PYTHON INTERMEDIÁRIO

### 1. Funções Avançadas

* `*args`: múltiplos argumentos posicionais
* `**kwargs`: múltiplos argumentos nomeados
* Funções como objetos: passar como argumento, retornar de função
* `lambda`: sintaxe e uso com `sort`, `map`

---

### 2. Funções de Ordem Superior

* `enumerate()`: índice + valor
* `zip()`: combinar listas
* `map()`: aplicar função
* `filter()`: filtrar com função

---

### 3. Iteradores e Geradores

* Conceito de iterável, `iter()`, `next()`
* `yield`: diferença de `return`
* Uso prático: processar dados sem carregar tudo em memória

---

### 4. Decorators

* Função que recebe função (wrapper)
* Conceito de `@decorator`
* Exemplo prático: medir tempo de execução

---

### 5. Type Hints

* Tipos em parâmetros e retorno
* `List[int]`, `Dict[str, int]`, `Optional[str]`
* Por que usar: documentação e IDE inteligente

---

### 🎯 Mini Projeto — BLOCO 2

* Criar funções reutilizáveis com type hints de:
  * Limpeza de dados
  * Transformação de formato
  * Validação de entrada

---

## 🔹 BLOCO 3 — PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)

### 1. Classes e Instâncias

* `class`, `__init__`, `self`
* Atributo de instância vs atributo de classe

### 2. Métodos

* Métodos comuns, métodos que retornam valores
* `__str__`, `__repr__` (representação)

### 3. Encapsulamento

* `_protegido`, `__privado` (convenção vs name mangling)

### 4. Herança

* Classe pai → classe filha
* `super()`
* Override de métodos

### 5. Composição

* Classe dentro de classe (preferível a herança profunda)

### 6. Organização de Projeto

* Separar classes em arquivos diferentes
* `import` entre arquivos do mesmo projeto

---

### 🎯 Mini Projeto — BLOCO 3

Implementar as classes:
* `Dataset` — carrega e armazena dados
* `Processor` — aplica transformações
* `Saver` — salva resultado em arquivo

---

## 🔹 BLOCO 4 — NUMPY (ULTRA DETALHADO)

NumPy é a base de toda computação numérica em Python — você vai usar isso em 100% das fases seguintes.

### Arrays

* Array 1D e 2D (e 3D para imagens)
* Criação: `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`

### Indexação e Slicing

* Posição simples e slicing multi-dimensional
* Boolean indexing: `arr[arr > 0]`

### Operações Vetorizadas

* Soma, subtração, multiplicação elemento a elemento
* **Broadcasting:** Regra de compatibilidade de shapes

> ⚠️ **Domínio crítico:** Nunca usar `for` onde uma operação NumPy resolve

### Álgebra Linear

* `np.dot`: produto escalar e multiplicação de matrizes
* `np.linalg.norm`, `np.linalg.inv`, `np.linalg.solve`

### Estatística

* `np.mean`, `np.std`, `np.median`, `np.percentile`

### Transformação

* `reshape`, `transpose`, `flatten`
* `np.concatenate`, `np.stack`, `np.split`

---

## 🔹 BLOCO 4.2 — PANDAS

### DataFrame

* Criação a partir de dict, lista, CSV
* Seleção de colunas e linhas (`.loc`, `.iloc`)

### Leitura e Escrita

* `read_csv()`, `to_csv()`

### Filtragem

* Condição simples e múltiplas condições com `&`, `|`

### Limpeza

* `dropna()`, `fillna()`, `duplicated()`, `drop_duplicates()`
* Detectar tipos: `dtypes`, converter: `astype()`

### Agrupamento e Agregação

* `groupby()`, `agg()`, `value_counts()`

### 🎯 Domínio

* Limpar dataset real sem tutorial

---

## 🔹 BLOCO 4.3 — MATPLOTLIB

### Gráficos Básicos

* `plot()` — linha
* `scatter()` — dispersão
* `bar()` / `barh()` — barras
* `hist()` — histograma

### Imagem

* `imshow()` — exibir array como imagem

### Customização

* `title()`, `xlabel()`, `ylabel()`
* `legend()`, `grid()`
* Múltiplos plots: `subplots()`

---

## 🔹 BLOCO 5 — AMBIENTE E BOAS PRÁTICAS

### Ambiente Virtual

* `venv`: criar e ativar
* `pip install`, `pip freeze > requirements.txt`
* Instalar de arquivo: `pip install -r requirements.txt`

### Jupyter Notebook

* Criar notebook, rodar células
* Diferença entre célula de código e markdown

### VSCode

* Extensões Python (Pylance, Python)
* Debugger: breakpoints, inspecionar variáveis

### Git (mínimo obrigatório)

* `git init`, `git add`, `git commit`, `git push`
* `.gitignore`: ignorar `venv/`, `*.pyc`, `data/`

---

## 🔹 BLOCO 6 — QUALIDADE DE CÓDIGO

### Complexidade Algorítmica (intuição)

* O(n) vs O(n²): por que importa
* Identificar loops desnecessários

### Código Limpo

* Nomes claros de variáveis e funções
* Funções pequenas com responsabilidade única
* Sem código morto ou comentários óbvios

### Docstrings

```python
def processar(dados: list) -> list:
    """
    Processa a lista de dados removendo nulos.

    Args:
        dados: Lista de valores a processar.

    Returns:
        Lista limpa sem valores None.
    """
```

### Logging

* `import logging`
* `logging.info()`, `logging.warning()`, `logging.error()`
* Por que não usar `print()` em produção

---

## 🧪 PROJETO FINAL (OBRIGATÓRIO)

### Pipeline completo de dados

**Estrutura do projeto:**

```
projeto_final/
├── data/
│   ├── raw/         ← CSV original
│   └── processed/   ← CSV limpo
├── dataset.py       ← Classe Dataset (carrega e valida)
├── processor.py     ← Classe Processor (limpa e transforma)
├── analysis.py      ← Funções de análise (médias, contagens)
├── utils.py         ← Funções auxiliares (logging, I/O)
└── main.py          ← Orquestra o pipeline
```

**Etapas obrigatórias:**

1. Leitura do CSV (Pandas)
2. Limpeza: remover nulos, corrigir tipos
3. Transformação: criar novas colunas derivadas
4. Análise: média, contagem por categoria
5. Visualização: pelo menos 2 gráficos
6. Saída: salvar CSV limpo + log das operações

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Tipos de dados e operações básicas
2. Estruturas de dados (listas, dicts, sets)
3. Condições e loops
4. List comprehension
5. Funções (básico → avançado → lambdas)
6. Iteradores e geradores
7. Decorators e type hints
8. Classes e POO
9. NumPy (arrays → operações → álgebra)
10. Pandas (carregar → filtrar → limpar → agrupar)
11. Matplotlib (visualização básica)
12. Ambiente (venv, pip, git)
13. Código limpo e logging
14. **Projeto Final**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Assistir aula sem implementar imediatamente depois
* Usar `for` onde o NumPy resolve (erro de principiante permanente)
* Não estruturar projeto em arquivos separados
* Ignorar erros sem ler a mensagem de traceback
* Copiar código sem entender cada linha

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 01 se:

* [ ] Não procura sintaxe básica de Python
* [ ] Consegue estruturar projeto em múltiplos arquivos sem tutorial
* [ ] Resolve mensagem de erro lendo o traceback
* [ ] Usa NumPy ao invés de loops onde possível
* [ ] Implementa POO de forma natural (não forçada)
* [ ] Código está organizado, com docstrings e logging


---

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

# FASE 03 — VISÃO COMPUTACIONAL CLÁSSICA

> **Posição na trilha:** Primeira fase 100% visual. Você aprende a "ver" imagens como dado.
> **Nível:** Intermediário
> **Tempo estimado:** 1 semana (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 00 e Fase 01 completas (NumPy sólido é crítico)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### NumPy (nível obrigatório)

* Criação de arrays: `np.array`, `np.zeros`, `np.ones`
* Indexação: 1D, 2D, 3D
* Slicing: `[linha, coluna]`, `[ :, : ]`
* Operações vetorizadas: soma, multiplicação
* Shape: `(altura, largura, canais)`

👉 **Domínio:** Manipular matriz **sem** usar loop sempre

---

### Álgebra Linear aplicada (mínimo)

* Vetor = lista de números
* Matriz = grade de números
* Multiplicação elemento a elemento
* Produto escalar (para convolução)

---

### Ferramentas obrigatórias (instalar antes de começar)

```bash
pip install opencv-python numpy matplotlib
```

* `cv2` (OpenCV) — processamento de imagem
* `numpy` — operações matriciais
* `matplotlib.pyplot` — visualização

---

## 🔹 BLOCO 1 — IMAGEM COMO MATRIZ (BASE REAL)

> Este é o conceito mais importante desta fase: **imagem = array NumPy**. Quando você entende isso, tudo o mais é operação matricial.

### Representação de Imagem

**RGB (3D)**
```
shape: (altura, largura, canais)
canais: 0 → Red, 1 → Green, 2 → Blue
Exemplo: (480, 640, 3)
```

**Grayscale (2D)**
```
shape: (altura, largura)
Exemplo: (480, 640)
```

**Faixa de valores**
* `uint8`: 0 a 255 (padrão)
* `float32`: 0.0 a 1.0 (para redes neurais)

### Acesso a Pixels

```python
img = cv2.imread("foto.jpg")  # Carrega como BGR (não RGB!)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converter para RGB

pixel = img[y, x]          # Valor do pixel (lista de 3 canais)
canal_r = img[y, x, 0]     # Canal R do pixel (x, y)
```

> ⚠️ **Armadilha clássica:** OpenCV carrega imagens em formato **BGR**, não RGB. Sempre converter se for exibir com matplotlib.

### Operações Básicas

**Crop (recorte)**
```python
recorte = img[y1:y2, x1:x2]
```

**Resize**
```python
menor = cv2.resize(img, (320, 240))
# Ou manter aspecto:
escala = 0.5
menor = cv2.resize(img, None, fx=escala, fy=escala)
```

**Conversão de cor**
```python
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
```

**Normalização**
```python
img_float = img.astype(np.float32) / 255.0
```

### Leitura e Escrita

```python
img = cv2.imread("entrada.jpg")
cv2.imwrite("saida.jpg", resultado)
```

### 🎯 Domínio

* Tratar imagem como array puro
* Manipular pixels sem "magia de biblioteca"

### 🚧 Exercício obrigatório

1. Ler imagem com OpenCV
2. Converter BGR → RGB
3. Aumentar brilho manualmente: `img_brilho = np.clip(img + 50, 0, 255).astype(np.uint8)`
4. Recortar região central
5. Salvar nova imagem

---

## 🔹 BLOCO 2 — CONVOLUÇÃO (BASE MATEMÁTICA DE CNN)

> Convolução é a operação central de toda rede neural para imagens. Implementar manualmente aqui é o que vai fazer você entender CNNs de verdade.

### O que é um Kernel (Filtro)

* Matriz pequena (geralmente 3×3 ou 5×5)
* Desliza sobre a imagem
* Em cada posição: multiplicação elemento a elemento + soma = 1 valor

### Operação Formal

```
Para cada posição (i, j) na imagem:
  resultado[i,j] = Σ (vizinhança[i-k, j-l] * kernel[k, l])
```

### Tipos de Filtros e seus Kernels

**Blur (suavização)**
```python
kernel_blur = np.ones((3, 3)) / 9  # Média dos 9 pixels vizinhos
```

**Detecção de borda horizontal (Sobel Y)**
```python
kernel_sobel_y = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
```

**Detecção de borda vertical (Sobel X)**
```python
kernel_sobel_x = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
```

**Sharpen (realce)**
```python
kernel_sharpen = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
```

### Implementação Manual (OBRIGATÓRIO)

```python
def convolver(imagem, kernel):
    """Convoluição manual — sem cv2.filter2D"""
    h, w = imagem.shape
    kh, kw = kernel.shape
    pad = kh // 2
    resultado = np.zeros_like(imagem, dtype=np.float32)
    
    img_padded = np.pad(imagem, pad, mode='constant')
    
    for i in range(h):
        for j in range(w):
            vizinhanca = img_padded[i:i+kh, j:j+kw]
            resultado[i, j] = np.sum(vizinhanca * kernel)
    
    return np.clip(resultado, 0, 255).astype(np.uint8)
```

**Com OpenCV (para comparar):**
```python
resultado = cv2.filter2D(img_gray, -1, kernel)
```

### 🎯 Domínio

* Entender: convolução = operação local que detecta padrão específico
* Saber que CNN aprende os kernels automaticamente (não são fixos)

### 🚧 Exercício obrigatório

1. Implementar convolução manual (código acima)
2. Aplicar kernel de blur, borda e sharpen
3. Comparar resultado manual com `cv2.filter2D` — devem ser idênticos

---

## 🔹 BLOCO 3 — TÉCNICAS CLÁSSICAS COM OPENCV

### Detecção de Borda

**Canny (mais robusto)**
```python
bordas = cv2.Canny(img_gray, threshold1=50, threshold2=150)
```
* `threshold1`: threshold baixo (conecta bordas fracas próximas de fortes)
* `threshold2`: threshold alto (define bordas fortes)

**Sobel (direcional)**
```python
grad_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(grad_x**2 + grad_y**2)
```

### Threshold (Binarização)

```python
_, binario = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Adaptativo (melhor para iluminação variável)
bin_adaptativo = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)
```

### Contornos (Contours)

```python
contours, _ = cv2.findContours(binario, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_cont = img.copy()
cv2.drawContours(img_cont, contours, -1, (0, 255, 0), 2)

# Área e bounding box de cada contorno
for c in contours:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
```

### Histogramas

```python
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title("Histograma de intensidade")
```

### Espaço de Cor HSV (CRÍTICO para detecção por cor)

```python
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Intervalo para detectar cor laranja
lower = np.array([10, 100, 100])
upper = np.array([25, 255, 255])
mascara = cv2.inRange(hsv, lower, upper)
resultado = cv2.bitwise_and(img, img, mask=mascara)
```

**Por que HSV?**
* H (Hue): matiz da cor (0-179 no OpenCV)
* S (Saturation): vivacidade
* V (Value): brilho
* Separar cor de iluminação = filtrar por cor funciona em diferentes luminosidades

### Transformações Geométricas

```python
# Translação
M = np.float32([[1, 0, tx], [0, 1, ty]])
deslocada = cv2.warpAffine(img, M, (w, h))

# Rotação
centro = (w//2, h//2)
M = cv2.getRotationMatrix2D(centro, angulo_graus, escala=1.0)
rotacionada = cv2.warpAffine(img, M, (w, h))

# Flip
espelhada = cv2.flip(img, 1)  # 0=vertical, 1=horizontal, -1=ambos
```

### 🚧 Mini-projeto — BLOCO 3

**Detector de cor em tempo real**
1. Abrir webcam
2. Converter frame para HSV
3. Criar máscara para uma cor específica (laranja, verde, etc.)
4. Exibir frame com máscara aplicada + contorno destacado

---

## 🔹 BLOCO 4 — PROCESSAMENTO DE VÍDEO

> Vídeo = sequência de imagens (frames). Cada frame é um array. O loop de processamento é a base de qualquer sistema de visão em tempo real.

### Leitura de Vídeo

```python
# Webcam
cap = cv2.VideoCapture(0)

# Arquivo de vídeo
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Processar frame aqui
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Resultado", gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Salvar Vídeo

```python
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('saida.mp4', fourcc, fps=30, frameSize=(w, h))

# No loop:
out.write(frame_processado)

out.release()
```

### Detecção de Movimento

```python
frame_anterior = None

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if frame_anterior is None:
        frame_anterior = gray
        continue
    
    diferenca = cv2.absdiff(frame_anterior, gray)
    thresh = cv2.threshold(diferenca, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) < 500:  # Ignorar ruído
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    frame_anterior = gray
```

### 🎯 Domínio

* Pensar em vídeo como: sequência de imagens
* Toda operação de imagem funciona frame a frame
* **Explicitamente necessário na Fase 07 (Object Detection em vídeo)**

### 🚧 Mini-projeto — BLOCO 4

* Detector de movimento com gravação automática quando detecta movimento

---

## 🧪 PROJETOS OBRIGATÓRIOS (DETALHADO)

### 1️⃣ Detector de Bordas

* Entrada: imagem qualquer
* Pré-processar (grayscale + blur)
* Aplicar Canny com threshold ajustável
* Saída: imagem original lado a lado com bordas detectadas

### 2️⃣ Detector por Cor (HSV)

* Converter para HSV
* Definir intervalo de cor com sliders interativos (`cv2.createTrackbar`)
* Criar máscara e highlight da região detectada

### 3️⃣ Detector de Movimento em Vídeo

* Capturar vídeo (webcam ou arquivo)
* Comparar frames consecutivos
* Destacar regiões com mudança
* Contar objetos em movimento com contornos

### 4️⃣ Pipeline de Pré-processamento de Imagem

* Receber imagem de qualquer tamanho e canal
* Normalizar para formato padrão: `(224, 224, 3)`, `float32`, valores 0-1
* Esta é a entrada padrão para redes neurais (preparação para Fase 05)

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Imagem como array (RGB, grayscale, shapes)
2. Acesso a pixels e slicing
3. Conversão de cores (BGR↔RGB, ↔Grayscale, ↔HSV)
4. Operações básicas (crop, resize, flip)
5. **Convolução manual** (loop NumPy)
6. Comparar com `cv2.filter2D`
7. Filtros clássicos (blur, borda, sharpen)
8. Canny e Sobel
9. Threshold (simples e adaptativo)
10. Contornos e bounding boxes
11. Histogramas
12. HSV e detecção por cor
13. Transformações geométricas
14. Vídeo: leitura de webcam
15. Detecção de movimento
16. **Projetos obrigatórios**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Usar OpenCV sem entender que é tudo array NumPy por baixo
* Pular a convolução manual (vai doer nas fases de CNN)
* Só assistir vídeo/aula — cada técnica tem que ser testada com imagem própria
* Não testar com imagens próprias (webcam, fotos suas)
* Esquecer de converter BGR → RGB ao usar matplotlib

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 04 se:

* [ ] Manipula imagem diretamente com NumPy (sem OpenCV quando possível)
* [ ] Explica como um filtro de convolução funciona matematicamente
* [ ] Implementa convolução manual que gera resultado igual ao OpenCV
* [ ] Processa vídeo em tempo real com pelo menos uma transformação
* [ ] Resolve problema simples (detecção por cor, detecção de movimento) **sem IA**
* [ ] Constrói pipeline de pré-processamento para formato de entrada de redes neurais


---

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

# FASE 05 — REDES NEURAIS CONVOLUCIONAIS (CNN)

> **Posição na trilha:** Aqui a IA começa a "ver" imagens de verdade — automaticamente aprende quais features extrair.
> **Nível:** Avançado
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fases 03 (convolução manual) e 04 (PyTorch sólido) completas

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Deep Learning (Fase 04 sólida)

* Entender forward pass e backpropagation
* Saber o que é tensor e como funciona `nn.Module`
* Treinar modelo simples no PyTorch **sem copiar tutorial**

👉 Se você ainda copia código → NÃO avance

### Imagem como Matriz (Fase 03)

* RGB = `(H, W, C)` → em PyTorch: `(C, H, W)`
* Manipular imagem com NumPy/OpenCV
* Entender o que é convolução manualmente

### PyTorch Prático

* Dataset + DataLoader funcionando
* Loop de treino completo
* Loss + Optimizer

---

## 🔹 BLOCO 1 — CONVOLUÇÃO (NÍVEL ENGENHEIRO)

> A diferença entre um usuário de CNN e um engenheiro de CNN é: o engenheiro consegue prever o shape da saída sem rodar o código.

### Anatomia da Camada Convolucional

**Parâmetros da `nn.Conv2d`:**

```python
nn.Conv2d(
    in_channels=3,     # Canais de entrada (3 para RGB)
    out_channels=32,   # Número de filtros (= feature maps na saída)
    kernel_size=3,     # Tamanho do kernel (3 = 3×3)
    stride=1,          # Passo do kernel
    padding=1,         # Borda adicionada para manter tamanho
    bias=True
)
```

### Fórmula de Shape da Saída (CRÍTICO)

```
H_out = floor((H_in + 2*padding - kernel_size) / stride) + 1
W_out = floor((W_in + 2*padding - kernel_size) / stride) + 1
```

**Exemplos práticos:**

| Entrada | kernel | stride | padding | Saída |
|---|---|---|---|---|
| (1, 3, 224, 224) | 3×3 | 1 | 1 | (1, 32, 224, 224) |
| (1, 3, 224, 224) | 3×3 | 2 | 1 | (1, 64, 112, 112) |
| (1, 3, 224, 224) | 7×7 | 2 | 3 | (1, 64, 112, 112) |

### Stride

* `stride=1` (padrão): kernel se move 1 pixel por vez
* `stride=2`: reduz dimensão por 2 (alternativa ao pooling)

### Padding

* `padding=0` ("valid"): saída menor que entrada
* `padding=kernel_size//2` ("same"): saída mantém dimensão

### 🎯 Domínio

* Conseguir prever shape da saída **sem rodar código**

### 🚧 Exercício obrigatório

1. Calcular shapes manualmente para 5 configs diferentes
2. Verificar com `x = torch.randn(1, 3, 224, 224); print(conv(x).shape)`

---

## 🔹 BLOCO 2 — FEATURE MAPS

> Cada filtro em uma camada Conv aprende a detectar um padrão específico. Com 32 filtros, você tem 32 "perspectivas" diferentes da imagem.

### O que são Feature Maps

```
Entrada: (1, 3, 224, 224)     ← 1 imagem RGB
              ↓ Conv2d(3→32, k=3)
Saída:   (1, 32, 224, 224)    ← 32 feature maps
```

Cada um dos 32 feature maps responde a um padrão diferente:
* Feature map 0: responde a bordas verticais
* Feature map 1: responde a bordas horizontais  
* Feature map 7: responde a cantos
* Feature map 20: responde a texturas específicas

### Visualizar Feature Maps

```python
# Extrair saída de uma camada
activation = {}
def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()
    return hook

model.conv1.register_forward_hook(get_activation('conv1'))
output = model(img_tensor)

# Plotar feature maps
fig, axes = plt.subplots(4, 8, figsize=(16, 8))
for i, ax in enumerate(axes.flat):
    if i < activation['conv1'].shape[1]:
        ax.imshow(activation['conv1'][0, i].numpy(), cmap='viridis')
    ax.axis('off')
```

---

## 🔹 BLOCO 3 — ARQUITETURA CNN COMPLETA

### Pipeline

```
Imagem (C, H, W)
    ↓
[Conv2d → BatchNorm → ReLU → MaxPool] × N    ← Blocos de extração
    ↓
Flatten ou AdaptiveAvgPool2d
    ↓
[Linear → ReLU → Dropout] × M                ← Classificador
    ↓
Linear → Softmax/Sigmoid                      ← Saída
```

### Pooling

**MaxPooling**
```python
nn.MaxPool2d(kernel_size=2, stride=2)
# Reduz H e W pela metade, mantém canais
# Pega o valor máximo em cada janela 2×2
```

**AveragePooling**
```python
nn.AvgPool2d(2, 2)
```

**Global Average Pooling (GAP)**
```python
nn.AdaptiveAvgPool2d(1)  # → shape (batch, channels, 1, 1)
# Alternativa ao Flatten — melhor para transfer learning
```

### Flatten

```python
nn.Flatten()  # (batch, C, H, W) → (batch, C*H*W)
# Ou: x.view(x.size(0), -1)
```

### 🎯 Domínio

* Entender o fluxo completo da imagem até a saída
* Saber calcular o shape em cada etapa

### 🚧 Exercício

* Desenhar no papel a arquitetura antes de codar
* Incluir shapes em cada camada

---

## 🔹 BLOCO 4 — PRIMEIRA CNN: MNIST → CIFAR-10

### CNN para MNIST

```python
class CNNMnist(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),  # (1,28,28)→(32,28,28)
            nn.ReLU(),
            nn.MaxPool2d(2, 2),              # (32,28,28)→(32,14,14)
            nn.Conv2d(32, 64, 3, padding=1), # (32,14,14)→(64,14,14)
            nn.ReLU(),
            nn.MaxPool2d(2, 2),              # (64,14,14)→(64,7,7)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),                    # (64,7,7)→(3136)
            nn.Linear(64*7*7, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 10)
        )
    
    def forward(self, x):
        return self.classifier(self.features(x))
```

**Meta:** > 99% accuracy em MNIST

### Evolução para CIFAR-10

**Diferenças:**
* 3 canais RGB (não 1)
* Imagens 32×32
* 10 classes mais difíceis (aviões, carros, pássaros...)
* Requer rede mais profunda

**Meta:** > 85% accuracy em CIFAR-10 (sem transfer learning)

---

## 🔹 BLOCO 5 — DATA AUGMENTATION

> Mais dados = melhor generalização. Data augmentation é a forma de "multiplicar" seu dataset artificialmente.

### Transformações com torchvision

```python
from torchvision import transforms

# Para TREINO (com augmentation):
transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=10),
    transforms.RandomCrop(32, padding=4),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Para VALIDAÇÃO/TESTE (sem augmentation!):
transform_val = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])
```

> ⚠️ **Nunca** aplicar augmentation em validação/teste — apenas no treino

### Normalização (por que esses valores?)

Os valores `[0.485, 0.456, 0.406]` são a média e desvio padrão calculados sobre o **ImageNet** (dataset de 1.2M imagens). Modelos pré-treinados esperam exatamente essa normalização.

### 🚧 Exercício

* Treinar CIFAR-10 com e sem augmentation
* Comparar curvas de loss e accuracy final (esperado: ~5-10% de ganho)

---

## 🔹 BLOCO 6 — ARQUITETURAS CLÁSSICAS (ENTENDER A EVOLUÇÃO)

> Não é para implementar todas do zero. É para entender por que cada uma foi criada e o problema que resolve.

### LeNet-5 (1998)

* Primeira CNN bem-sucedida
* 2 camadas conv + 3 FC
* Base conceitual de tudo

### AlexNet (2012)

* Venceu ImageNet com margem absurda
* Trouxe: ReLU, dropout, GPU training
* Prova que CNN profunda funciona

### VGG (2014)

* Kernels sempre 3×3 (descoberta: profundidade > kernel grande)
* VGG16 e VGG19 ainda usados em transfer learning

### ResNet (2015) — CRÍTICO

**O problema:** Redes muito profundas sofrem de "degradação" — adicionar mais camadas piora o resultado. Por quê? Gradiente desaparece nas primeiras camadas.

**A solução — Skip Connection:**

```python
# Bloco residual simples
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)
    
    def forward(self, x):
        residual = x                          # ← Guardar entrada
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out = out + residual                  # ← Somar com entrada original
        return F.relu(out)
```

**Por que funciona:** O gradiente tem um "caminho direto" pelas skip connections — não precisa atravessar as camadas convolucionais (que podem sumir o gradiente).

### EfficientNet (2019)

* Escala largura, profundidade e resolução de forma balanceada
* Atualmente um dos mais usados em produção real

---

## 🔹 BLOCO 7 — TRANSFER LEARNING (MUNDO REAL)

> 90% dos projetos reais de visão não treinam CNN do zero. Usam transfer learning.

### Por que funciona?

Redes treinadas no ImageNet aprenderam features universais:
* Camadas iniciais: detectam bordas, cores, texturas
* Camadas intermediárias: detectam partes (olhos, rodas)
* Camadas finais: detectam objetos completos

Para um novo problema, você aproveita tudo isso e só treina as últimas camadas.

### Estratégias

**1. Feature Extraction (camadas congeladas)**
```python
modelo = torchvision.models.resnet50(pretrained=True)

# Congelar todas as camadas
for param in modelo.parameters():
    param.requires_grad = False

# Substituir apenas a última camada
num_classes = 5
modelo.fc = nn.Linear(modelo.fc.in_features, num_classes)
# Só `modelo.fc` tem requires_grad=True
```

**2. Fine-Tuning (camadas descongeladas gradualmente)**
```python
# Descongelar últimas N camadas
for param in modelo.layer4.parameters():
    param.requires_grad = True

# Usar lr menor para não destruir features pré-treinadas
otimizador = torch.optim.Adam([
    {'params': modelo.layer4.parameters(), 'lr': 1e-4},
    {'params': modelo.fc.parameters(), 'lr': 1e-3}
])
```

**Quando usar qual:**
* Dataset pequeno + similar ao ImageNet → Feature extraction
* Dataset médio → Fine-tuning das últimas camadas
* Dataset grande → Fine-tuning de tudo (ou treinar do zero)

### 🚧 Projetos

1. **Gatos vs Cachorros:** ResNet18 com feature extraction — deve atingir > 95% com dataset de 1000 imagens
2. **Dataset próprio:** Criar dataset com suas próprias fotos (mínimo 3 classes, 100 imagens por classe)

---

## 🔹 BLOCO 8 — VISION TRANSFORMERS (ViT) — INTRODUÇÃO

> ViT não usa convolução. Divide a imagem em patches (pedaços) e aplica o mecanismo de atenção — o mesmo de modelos de linguagem.

### Por que estudar aqui?

Na **Fase 06 (NLP & Transformers)** você vai aprender o mecanismo de atenção em profundidade. Este bloco é uma **introdução conceitual** — você vai entender completamente na próxima fase.

### Conceito

```
Imagem (224×224)
    ↓
Dividir em patches de 16×16 → 196 patches
    ↓
Cada patch → vetor de embedding (como token de texto)
    ↓
Position encoding (manter informação espacial)
    ↓
Self-Attention entre todos os patches
    ↓
Classificação
```

### CNN vs ViT

| | CNN | ViT |
|---|---|---|
| Receptive field | Local (vizinhança imediata) | Global (todos os patches) |
| Inductive bias | Sim (localidade, equivariância) | Mínimo |
| Dado necessário | Menos dados | Muito mais dados |
| Performance | Excelente em datasets médios | Estado da arte em datasets grandes |

### Uso prático hoje

```python
import timm

modelo = timm.create_model('vit_base_patch16_224', pretrained=True, num_classes=10)
```

### 🎯 Domínio

* Entender a diferença conceitual CNN vs ViT
* Saber quando um é melhor que o outro
* **Implementação completa na Fase 06**

---

## 🧪 PROJETOS OBRIGATÓRIOS

### 1️⃣ CNN do zero (MNIST)

* Arquitetura sua (não copiar)
* > 99% accuracy

### 2️⃣ CNN CIFAR-10

* 3 canais RGB
* Comparar: com e sem data augmentation
* > 85% accuracy

### 3️⃣ Transfer Learning com ResNet

* Congelar camadas + trocar head
* Dataset próprio (suas fotos)
* > 90% accuracy com > 3 classes

### 4️⃣ Análise de erros

* Visualizar os 20 exemplos que o modelo mais errou
* Formular hipótese sobre por que errou
* Aplicar melhoria baseada na hipótese

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Fórmula de shape de convolução (praticar manualmente)
2. `nn.Conv2d` no PyTorch + visualizar saída
3. MaxPooling, Average Pooling, GAP
4. Arquitectura CNN completa (papel → código)
5. MNIST com CNN
6. CIFAR-10 (aumentar complexidade)
7. Data augmentation (comparar com e sem)
8. Arquiteturas clássicas (LeNet → ResNet, entender evolução)
9. Skip connections (ResNet — implementar bloco residual)
10. Transfer learning — feature extraction
11. Transfer learning — fine-tuning
12. Dataset próprio
13. ViT (conceito + uso com `timm`)
14. **Análise de erros (projeto 4)**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Não entender shape → erro número 1 em CNN
* Copiar arquitetura pronta sem entender cada camada
* Ignorar overfitting (treino alto, val baixo)
* Não usar data augmentation
* Pular transfer learning (irrealista no mercado — ninguém treina ResNet do zero)
* Aplicar normalização errada ao usar modelo pré-treinado

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 06 se:

* [ ] Constrói CNN do zero e explica cada camada e shape
* [ ] Ajusta modelo sozinho baseado nas curvas de loss
* [ ] Usa transfer learning corretamente (normalização certa, lr diferenciado)
* [ ] Resolve problema real com imagens próprias (> 90% accuracy)
* [ ] Entende a diferença conceitual entre CNN e ViT
* [ ] Analisa erros do modelo e aplica melhoria justificada


---

# FASE 06 — NLP & TRANSFORMERS (PONTE PARA IA MODERNA)

> **Posição na trilha:** NOVA FASE. Ponte obrigatória entre CNNs e IA Generativa/Multimodal.
> **Por que aqui?** ViT, CLIP, Stable Diffusion, GPT-4V — todos dependem de Transformers. Sem esta fase, a Fase 10 (Generativa) não faz sentido.
> **Nível:** Avançado
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 04 (backprop, PyTorch) e Fase 05 (conceito de ViT)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Deep Learning (Fase 04)

* Backpropagation com regra da cadeia
* `nn.Module`, loops de treino, otimizadores

### CNNs (Fase 05)

* Feature maps, embeddings visuais
* Conceito introdutório de ViT (Bloco 8 da Fase 05)

### Matemática (Fase 01)

* Produto escalar (dot product)
* Multiplicação de matrizes
* Softmax

### Estratégia desta fase

* Foco em **Transformers para Visão** (não em NLP extenso)
* NLP aqui é a ponte — você não vai virar engenheiro de LLM
* O que você **precisa** saber: tokenização, embeddings, atenção, CLIP
* O que você **não precisa** agora: RLHF, fine-tuning de LLMs, RAG

---

## 🔹 BLOCO 1 — REPRESENTAÇÃO DE TEXTO EM NÚMEROS

> Antes de qualquer Transformer, você precisa entender: como texto vira vetor?

### Tokenização

```python
# Texto → lista de tokens (subpalavras)
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer("Um cachorro correndo no parque")
# {'input_ids': [101, 1041, 3232, ..., 102], 'attention_mask': [1,1,...]}
```

**Tipos de tokenização:**
* Word-level: cada palavra = token (vocabulário enorme, palavras desconhecidas)
* Char-level: cada caractere = token (sem OOV, mas sequências longas)
* **Subword (BPE/WordPiece):** palavras comuns inteiras, palavras raras em partes — melhor equilíbrio

### Embeddings

**Word Embedding:** Mapear token (inteiro) → vetor denso (ex: 512 dimensões)

```python
# Camada de embedding
embedding = nn.Embedding(num_embeddings=30000, embedding_dim=512)

# token_id → vetor
vetor = embedding(torch.tensor([42]))  # shape (1, 512)
```

**Por que embedding?**
* `cachorro` e `cão` → vetores próximos
* `cachorro` e `avião` → vetores distantes
* A proximidade no espaço latente captura semântica

**Embeddings de posição (CRÍTICO)**
```python
# Transformer não sabe ordem naturalmente — precisa de position encoding
# Opção 1: Embedding treinável
pos_embedding = nn.Embedding(max_seq_len, d_model)

# Opção 2: Sinusoidal (original do paper "Attention Is All You Need")
# PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
# PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

---

## 🔹 BLOCO 2 — MECANISMO DE ATENÇÃO (CORAÇÃO DO TRANSFORMER)

> Este é o conceito central de toda a IA moderna. Entender atenção = entender GPT, ViT, CLIP, Stable Diffusion.

### Intuição

**Problema:** Ao traduzir "O banco do rio é bonito", como saber que "banco" é margem (não instituição financeira)?

**Solução da atenção:** Ao processar cada palavra, olhar para **todas as outras palavras** e calcular quanta atenção dar a cada uma.

### Scaled Dot-Product Attention

```
Entradas:
  Q (Query)  = "o que estou procurando?"
  K (Key)    = "o que cada token pode oferecer?"
  V (Value)  = "o que cada token realmente contém?"

Operação:
  Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V
```

**Implementação manual:**

```python
import torch
import torch.nn.functional as F

def attention(Q, K, V, mask=None):
    d_k = Q.shape[-1]
    
    # Scores de atenção
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    
    # Opcional: máscara (ex: tokens de padding)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    
    # Softmax → pesos de atenção (somam 1)
    pesos = F.softmax(scores, dim=-1)
    
    # Ponderação dos valores
    return torch.matmul(pesos, V)
```

**Intuição dos pesos:** Se a palavra "rio" recebe peso 0.8 ao processar "banco", a representação final de "banco" vai ser 80% do embedding de "rio" + outras contribuições.

### Multi-Head Attention

```python
# Ao invés de 1 atenção de dimensão d_model,
# usar H atenções paralelas de dimensão d_model/H

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_k = d_model // num_heads
        self.num_heads = num_heads
        
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
    
    def split_heads(self, x):
        B, seq, d = x.shape
        return x.view(B, seq, self.num_heads, self.d_k).transpose(1, 2)
    
    def forward(self, Q, K, V, mask=None):
        Q = self.split_heads(self.W_q(Q))  # (B, H, seq, d_k)
        K = self.split_heads(self.W_k(K))
        V = self.split_heads(self.W_v(V))
        
        attn = attention(Q, K, V, mask)    # (B, H, seq, d_k)
        
        # Concatenar todas as heads
        B, H, seq, d_k = attn.shape
        attn = attn.transpose(1, 2).contiguous().view(B, seq, H*d_k)
        
        return self.W_o(attn)
```

**Por que múltiplas heads?** Cada head aprende a "olhar" para aspectos diferentes da frase:
* Head 1: relações sintáticas (sujeito ↔ verbo)
* Head 2: correferência (pronome ↔ substantivo)
* Head 3: posição relativa

---

## 🔹 BLOCO 3 — ARQUITETURA TRANSFORMER COMPLETA

### Bloco Transformer Encoder

```
Input embeddings + Position encoding
        ↓
┌─────────────────────────────────┐
│  Multi-Head Self-Attention      │
│          + residual + LayerNorm │
├─────────────────────────────────┤
│  Feed-Forward Network           │
│  (Linear → ReLU/GELU → Linear) │
│          + residual + LayerNorm │
└─────────────────────────────────┘
         × N camadas
        ↓
Output: representações contextuais
```

### Self-Attention vs Cross-Attention

**Self-Attention:** Q, K, V vêm da mesma sequência
* Usado em encoder (texto analisa a si mesmo)
* Usado em decoder para análise do output gerado

**Cross-Attention:** Q vem de uma sequência, K e V de outra
* Conecta encoder ao decoder
* **CRÍTICO para visão:** Como texto guia geração de imagem (Q=texto, K,V=imagem)

### Tipos de Transformer

**Encoder-only (BERT):** Representa texto → usado para classificação, NER
**Decoder-only (GPT):** Gera texto → autorregressivo
**Encoder-Decoder (T5, bart):** Sequência → sequência → tradução, sumarização

---

## 🔹 BLOCO 4 — VISION TRANSFORMER (ViT) COMPLETO

> Agora que você entende atenção, ViT faz sentido completo.

### Como a Imagem Vira "Tokens"

```python
class PatchEmbedding(nn.Module):
    def __init__(self, img_size=224, patch_size=16, in_channels=3, d_model=768):
        super().__init__()
        self.num_patches = (img_size // patch_size) ** 2  # 196 patches
        # Conv2d com stride=patch_size extrai patches eficientemente
        self.proj = nn.Conv2d(in_channels, d_model, kernel_size=patch_size, stride=patch_size)
    
    def forward(self, x):
        x = self.proj(x)                    # (B, d_model, H/p, W/p)
        x = x.flatten(2)                    # (B, d_model, num_patches)
        x = x.transpose(1, 2)              # (B, num_patches, d_model)
        return x

# CLS token: token especial para classificação (como em BERT)
cls_token = nn.Parameter(torch.zeros(1, 1, d_model))
# Position embedding: aprendível
pos_embed = nn.Parameter(torch.randn(1, num_patches + 1, d_model))
```

### Vantagem sobre CNN

* CNN: cada neurônio vê apenas vizinhança local
* ViT: cada patch "vê" todos os outros desde a primeira camada (atenção global)
* Para imagens grandes e alta resolução: ViT tende a ser superior com dados suficientes

### 🚧 Exercício

* Implementar ViT simplificado (2-4 camadas) para CIFAR-10
* Comparar com CNN equivalente em número de parâmetros

---

## 🔹 BLOCO 5 — CLIP (CONECTANDO TEXTO E IMAGEM)

> CLIP é o modelo que faz tudo multimodal funcionar: ViT, Stable Diffusion, DALL-E, GPT-4V.

### Como o CLIP Funciona

```
Imagem → Image Encoder (ViT) → vetor de imagem (512d)
Texto  → Text Encoder (Transformer) → vetor de texto (512d)

Treinamento: Contrastive Learning
  - Pares corretos (imagem, legenda) → maximizar similaridade
  - Pares errados → minimizar similaridade
```

### Por que é Revolucionário

* Zero-shot classification: sem treino extra
```python
from PIL import Image
import clip

model, preprocess = clip.load("ViT-B/32")

image = preprocess(Image.open("foto.jpg")).unsqueeze(0)
text = clip.tokenize(["um gato", "um cachorro", "um pássaro"])

with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    
    # Similaridade cosseno
    logits = (image_features @ text_features.T)
    probs = logits.softmax(dim=-1)

print(f"Gato: {probs[0,0]:.2%}, Cachorro: {probs[0,1]:.2%}")
```

### CLIP como Pré-requisito para Stable Diffusion

No Stable Diffusion:
1. Seu prompt de texto → CLIP Text Encoder → vetor de embedding
2. Esse vetor é injetado via **cross-attention** na U-Net
3. A U-Net usa esse vetor para "guiar" o processo de denoising

**Por isso esta fase vem antes da Fase 10 (Generativa).**

---

## 🔹 BLOCO 6 — USANDO HUGGING FACE (PRÁTICO)

> A biblioteca padrão da indústria para Transformers.

```python
from transformers import pipeline, AutoModel, AutoTokenizer

# Zero-shot com pipeline
classifier = pipeline("zero-shot-classification")
resultado = classifier(
    "Esta câmera tem ótima qualidade de imagem",
    candidate_labels=["eletrônicos", "comida", "esporte"]
)

# Extrair embeddings de texto
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

inputs = tokenizer(["frase 1", "frase 2"], return_tensors="pt", padding=True)
outputs = model(**inputs)
embeddings = outputs.last_hidden_state.mean(dim=1)  # Mean pooling

# Similaridade
from torch.nn.functional import cosine_similarity
sim = cosine_similarity(embeddings[0], embeddings[1], dim=0)
```

---

## 🧪 PROJETO FINAL (OBRIGATÓRIO)

### Classificador Zero-Shot com CLIP + Busca Visual

**Objetivo:** Sistema que recebe texto e encontra imagens correspondentes em um dataset.

**Etapas:**

1. Coletar dataset de imagens (ex: 1000 imagens de 10 categorias)
2. Calcular embeddings CLIP para todas as imagens (offline)
3. Interface: usuário digita texto, sistema retorna as 5 imagens mais similares
4. Comparar com classificador CNN treinado na mesma tarefa
5. Analisar casos onde CLIP vence a CNN e vice-versa

**Bônus:** Implementar attention rollout — visualizar quais patches da imagem o ViT "prestou mais atenção"

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Tokenização (conceito + prática com HuggingFace)
2. Embeddings e espaço semântico
3. Position encoding
4. Scaled Dot-Product Attention (implementar do zero)
5. Multi-Head Attention
6. Bloco Transformer Encoder completo
7. Self-Attention vs Cross-Attention
8. ViT: Patch Embedding
9. ViT: implementar e treinar em CIFAR-10
10. CLIP: conceito e uso
11. Zero-shot classification com CLIP
12. HuggingFace: pipelines e extração de embeddings
13. **Projeto Final: Busca visual com CLIP**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Tentar aprender NLP completo (tradução, geração, RLHF) — não é o objetivo aqui
* Usar HuggingFace sem entender o que há por baixo
* Pular implementação manual da atenção
* Não conectar esta fase com Stable Diffusion (Fase 10) — mantenha o "para que serve" em mente

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 07 se:

* [ ] Implementa Self-Attention do zero no PyTorch
* [ ] Explica como o texto guia a geração de imagens (cross-attention)
* [ ] Usa CLIP para classificação zero-shot sem tutorial aberto
* [ ] Entende a diferença entre CNN (local) e ViT (global)
* [ ] Extrai embeddings de texto e compara por similaridade semântica
* [ ] Constrói sistema de busca visual baseado em CLIP


---

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

**YOLO, SSD, RetinaFocal Loss**

```
Imagem
  ↓
Backbone (CNN/ViT)             ← Extrai features
  ↓
Grid de predições              ← Cada célula do grid prediz bboxes + classes
  ↓
NMS                            ← Remove duplicatas
```

**Quando usar:** Velocidade importante (webcam, edge, vídeo em tempo real)

### DETR (Detection Transformer) — Contexto

* Usa Transformer (atenção) para detecção
* Não precisa de NMS (atenção aprende a não duplicar)
* Requer mais dados e treino mais longo
* **Relevante com a Fase 06** — atenção cross entre features da imagem e queries de objeto

---

## 🔹 BLOCO 4 — YOLO NA PRÁTICA

### Por que YOLO?

* Mais rápido da categoria one-stage
* Ultraltyics YOLO = melhor DX da indústria
* YOLOv8/YOLOv11: estado da arte em velocidade/precisão

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
11. Tracking com ByteTrack
12. Exportar ONNX / TensorRT
13. Debug e melhoria

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


---

# FASE 08 — SEGMENTAÇÃO

> **Posição na trilha:** Evolução de bounding box para previsão pixel a pixel — cada pixel recebe uma classe.
> **Nível:** Avançado
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fases 05 (CNN sólida) e 07 (Object Detection)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### CNN (Fase 05 sólida)

* Convolução, feature maps, pooling
* Controle de shape (CRÍTICO — shapes são mais complexos aqui)

### Object Detection (Fase 07)

* Bounding box, IoU
* Dataset e anotação
* Treino com YOLO

👉 Segmentação é evolução direta de detecção

### PyTorch

* Dataset customizado, DataLoader
* Loop de treino completo

---

## 🔹 BLOCO 1 — TIPOS DE SEGMENTAÇÃO

### Segmentação Semântica

* Cada pixel → classe global (pessoa, carro, fundo)
* Todos os pixels da mesma classe = mesma "cor"
* Não distingue instâncias separadas (duas pessoas = mesmo rótulo)

```
Entrada: (3, H, W) RGB
Saída:   (num_classes, H, W) — mapa de probabilidades por classe
         ou (H, W) — mapa de classes (argmax)
```

### Segmentação de Instâncias

* Cada pixel → instância específica de objeto
* Pessoa 1 ≠ Pessoa 2 mesmo sendo da mesma classe
* Combina detecção + segmentação

### Segmentação Panóptica

* Unifica semântica + instâncias
* "Stuff" (fundo, céu, grama) → semântico
* "Things" (pessoas, carros) → instâncias
* Estado da arte completo

---

## 🔹 BLOCO 2 — REPRESENTAÇÃO DE MÁSCARA (CRÍTICO)

### Máscara Binária

```python
# 0 → fundo, 1 → objeto
mascara = np.zeros((H, W), dtype=np.uint8)
mascara[100:200, 150:300] = 1  # Região do objeto
```

### Máscara Multi-classe

```python
# Cada pixel = inteiro representando a classe
mascara = np.zeros((H, W), dtype=np.uint8)
# 0 = fundo, 1 = pessoa, 2 = carro, 3 = bicicleta...
```

### One-Hot Encoding

```python
# Para loss: (num_classes, H, W) — cada canal = mapa binário de uma classe
def to_one_hot(mascara, num_classes):
    one_hot = np.zeros((num_classes, *mascara.shape))
    for c in range(num_classes):
        one_hot[c] = (mascara == c).astype(float)
    return one_hot
```

### Estrutura do Dataset de Segmentação

```
dataset/
├── images/
│   ├── train/
│   │   ├── img001.jpg
│   │   └── img002.jpg
│   └── val/
│       └── img003.jpg
└── masks/
    ├── train/
    │   ├── img001.png    ← MESMO nome, extensão .png
    │   └── img002.png    ← Máscara: pixels com valor da classe
    └── val/
        └── img003.png
```

**Regra crítica:** Imagem e máscara devem ter:
* Mesmo nome de arquivo
* Mesma dimensão `(H, W)`
* A máscara é aplicada pixel-a-pixel

### Carregar e Visualizar

```python
import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread("images/train/img001.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mascara = cv2.imread("masks/train/img001.png", cv2.IMREAD_GRAYSCALE)

# Overlay da máscara na imagem
def overlay_mascara(img, mascara, alpha=0.5):
    colormap = plt.cm.get_cmap('tab10', mascara.max() + 1)
    mascara_cor = (colormap(mascara)[:, :, :3] * 255).astype(np.uint8)
    return cv2.addWeighted(img, 1-alpha, mascara_cor, alpha, 0)

resultado = overlay_mascara(img, mascara)
```

### Dataset PyTorch Customizado

```python
class SegmentationDataset(Dataset):
    def __init__(self, img_dir, mask_dir, transform=None, mask_transform=None):
        self.img_paths = sorted(glob(f"{img_dir}/*.jpg"))
        self.mask_paths = sorted(glob(f"{mask_dir}/*.png"))
        self.transform = transform
        self.mask_transform = mask_transform
    
    def __len__(self):
        return len(self.img_paths)
    
    def __getitem__(self, idx):
        img = Image.open(self.img_paths[idx]).convert("RGB")
        mask = Image.open(self.mask_paths[idx])
        
        # CRÍTICO: mesma transformação geométrica em imagem E máscara
        if self.transform:
            img = self.transform(img)
        if self.mask_transform:
            mask = self.mask_transform(mask)
        
        return img, mask
```

> ⚠️ **Armadilha:** Data augmentation geométrico (flip, rotação) deve ser aplicado **igualmente** à imagem e à máscara. Nunca separadamente.

### 🚧 Exercício obrigatório

1. Carregar par (imagem, máscara)
2. Exibir lado a lado
3. Sobrepor máscara colorida na imagem
4. Verificar alinhamento pixel a pixel

---

## 🔹 BLOCO 3 — FUNÇÕES DE PERDA (CRÍTICO)

### Binary Cross-Entropy (BCE)

```python
# Para segmentação binária (1 classe)
criterio = nn.BCEWithLogitsLoss()
loss = criterio(predicao, mascara.float())
```

### Dice Loss

```python
def dice_loss(pred, target, smooth=1.0):
    pred = torch.sigmoid(pred)
    pred = pred.view(-1)
    target = target.view(-1)
    
    intersecao = (pred * target).sum()
    dice = (2. * intersecao + smooth) / (pred.sum() + target.sum() + smooth)
    return 1 - dice
```

* Mede sobreposição entre predição e máscara real
* Especialmente útil quando objeto ocupa pequena fração da imagem

### Focal Loss

```python
def focal_loss(pred, target, alpha=0.25, gamma=2):
    bce = F.binary_cross_entropy_with_logits(pred, target, reduction='none')
    pt = torch.exp(-bce)
    focal = alpha * (1 - pt) ** gamma * bce
    return focal.mean()
```

* Foca em exemplos difíceis (pixels na borda, casos raros)
* Reduz peso de exemplos fáceis que dominam o treino

### Combinação Prática

```python
def combined_loss(pred, target, bce_weight=0.5, dice_weight=0.5):
    bce = F.binary_cross_entropy_with_logits(pred, target)
    dice = dice_loss(pred, target)
    return bce_weight * bce + dice_weight * dice
```

### 🎯 Domínio

| Cenário | Loss recomendada |
|---|---|
| Segmentação binária, classes balanceadas | BCE |
| Segmentação binária, objeto pequeno | Dice ou BCE + Dice |
| Múltiplas classes, desbalanceado | Focal Loss |
| Produção geral | BCE + Dice (combinação) |

---

## 🔹 BLOCO 4 — U-NET (ARQUITETURA BASE DA INDÚSTRIA)

> U-Net é usada em praticamente todos os projetos sérios de segmentação: médica, satélite, industrial.

### Arquitetura

```
Entrada (3, 256, 256)
│
├─ [Conv → BN → ReLU] × 2 → MaxPool    (encoder nível 1: 64ch, 128×128)
├─ [Conv → BN → ReLU] × 2 → MaxPool    (encoder nível 2: 128ch, 64×64)
├─ [Conv → BN → ReLU] × 2 → MaxPool    (encoder nível 3: 256ch, 32×32)
├─ [Conv → BN → ReLU] × 2 → MaxPool    (encoder nível 4: 512ch, 16×16)
│
└─ BOTTLENECK (1024ch, 8×8)
│
├─ UpConv + Concatenar com encoder 4   → (512ch, 16×16)
├─ UpConv + Concatenar com encoder 3   → (256ch, 32×32)
├─ UpConv + Concatenar com encoder 2   → (128ch, 64×64)
├─ UpConv + Concatenar com encoder 1   → (64ch, 128×128)
│
└─ Conv 1×1 → Saída (num_classes, 256, 256)
```

### Implementação PyTorch

```python
class DoubleConv(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )
    def forward(self, x):
        return self.conv(x)

class UNet(nn.Module):
    def __init__(self, in_channels=3, num_classes=1):
        super().__init__()
        
        # Encoder
        self.e1 = DoubleConv(in_channels, 64)
        self.e2 = DoubleConv(64, 128)
        self.e3 = DoubleConv(128, 256)
        self.e4 = DoubleConv(256, 512)
        self.bottleneck = DoubleConv(512, 1024)
        self.pool = nn.MaxPool2d(2, 2)
        
        # Decoder
        self.up4 = nn.ConvTranspose2d(1024, 512, 2, stride=2)
        self.d4 = DoubleConv(1024, 512)  # 512 (up) + 512 (skip) = 1024
        self.up3 = nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.d3 = DoubleConv(512, 256)
        self.up2 = nn.ConvTranspose2d(256, 128, 2, stride=2)
        self.d2 = DoubleConv(256, 128)
        self.up1 = nn.ConvTranspose2d(128, 64, 2, stride=2)
        self.d1 = DoubleConv(128, 64)
        
        self.final = nn.Conv2d(64, num_classes, 1)
    
    def forward(self, x):
        # Encoder
        s1 = self.e1(x)
        s2 = self.e2(self.pool(s1))
        s3 = self.e3(self.pool(s2))
        s4 = self.e4(self.pool(s3))
        b = self.bottleneck(self.pool(s4))
        
        # Decoder com skip connections
        d4 = self.d4(torch.cat([self.up4(b), s4], dim=1))
        d3 = self.d3(torch.cat([self.up3(d4), s3], dim=1))
        d2 = self.d2(torch.cat([self.up2(d3), s2], dim=1))
        d1 = self.d1(torch.cat([self.up1(d2), s1], dim=1))
        
        return self.final(d1)
```

### Por que Skip Connections?

* O encoder comprime informação (perde detalhes espaciais)
* O decoder precisa reconstruir a máscara na resolução original
* **Skip connections passam detalhes finos direto do encoder para o decoder**
* Sem skip connections: máscara reconstruída fica "borrada"

---

## 🔹 BLOCO 5 — VISUALIZAÇÃO E DEBUG (OBRIGATÓRIO)

```python
def plotar_predicao(img, mascara_real, mascara_pred, threshold=0.5):
    """Plotar imagem, máscara real e máscara predita lado a lado."""
    pred_bin = (torch.sigmoid(mascara_pred) > threshold).float()
    
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    axes[0].imshow(img.permute(1,2,0).numpy())
    axes[0].set_title("Imagem Original")
    axes[1].imshow(mascara_real.squeeze().numpy(), cmap='gray')
    axes[1].set_title("Máscara Real")
    axes[2].imshow(pred_bin.squeeze().numpy(), cmap='gray')
    axes[2].set_title("Máscara Predita")
    
    # Overlay
    overlay = img.permute(1,2,0).numpy().copy()
    overlay[pred_bin.squeeze().numpy() > 0] = [255, 0, 0]  # Vermelho
    axes[3].imshow(overlay)
    axes[3].set_title("Overlay")
    
    plt.tight_layout()
    plt.show()
```

**O que observar:**
* Bordas mal definidas → modelo precisa de mais dados ou imagens maiores
* Buracos dentro de objetos → post-processing (preenchimento morfológico)
* Falsos positivos em textura → dataset mais variado

---

## 🔹 BLOCO 6 — MÉTRICAS DE SEGMENTAÇÃO

### IoU por Pixel (Jaccard Index)

```python
def iou_score(pred, target, threshold=0.5):
    pred_bin = (torch.sigmoid(pred) > threshold).float()
    intersecao = (pred_bin * target).sum()
    uniao = pred_bin.sum() + target.sum() - intersecao
    return (intersecao + 1e-6) / (uniao + 1e-6)
```

### Dice Coefficient (F1 de pixels)

```python
def dice_score(pred, target, threshold=0.5):
    pred_bin = (torch.sigmoid(pred) > threshold).float()
    intersecao = (pred_bin * target).sum()
    return (2 * intersecao + 1e-6) / (pred_bin.sum() + target.sum() + 1e-6)
```

### Pixel Accuracy

```python
def pixel_accuracy(pred, target, threshold=0.5):
    pred_bin = (torch.sigmoid(pred) > threshold).float()
    return (pred_bin == target).float().mean()
```

### 🎯 Interpretação

| Métrica | Bom | Aceitável |
|---|---|---|
| IoU (segmentação médica) | > 0.85 | > 0.70 |
| Dice | > 0.90 | > 0.75 |
| IoU (segmentação geral) | > 0.70 | > 0.55 |

---

## 🔹 BLOCO 7 — PÓS-PROCESSAMENTO

```python
import cv2

def pos_processar_mascara(mascara_bin):
    """Limpar máscara após threshold."""
    # Remover pequenos ruídos
    kernel = np.ones((5,5), np.uint8)
    sem_ruido = cv2.morphologyEx(mascara_bin, cv2.MORPH_OPEN, kernel)
    
    # Fechar buracos dentro de objetos
    fechada = cv2.morphologyEx(sem_ruido, cv2.MORPH_CLOSE, kernel)
    
    # Dilatação leve nas bordas
    dilatada = cv2.dilate(fechada, kernel, iterations=1)
    
    return dilatada

# Usar após predição do modelo
pred_np = (torch.sigmoid(pred) > 0.5).squeeze().numpy().astype(np.uint8)
pred_limpa = pos_processar_mascara(pred_np)
```

**Operações morfológicas:**
* **Erosão:** Remove pixels de borda (elimina ruídos finos)
* **Dilatação:** Adiciona pixels de borda (expande regiões)
* **Opening (erosão + dilatação):** Remove ruído sem mudar forma
* **Closing (dilatação + erosão):** Fecha buracos sem mudar forma

---

## 🔹 BLOCO 8 — MASK R-CNN (SEGMENTAÇÃO DE INSTÂNCIAS)

> Mask R-CNN combina detecção com segmentação. É mais complexo que U-Net — proporcional ao que resolve.

### Componentes

```
Imagem
  ↓
Backbone (ResNet + FPN)        ← Extrai features multi-escala
  ↓
Region Proposal Network (RPN)  ← Propõe ~2000 regiões candidatas
  ↓
ROI Align                      ← Extrai features fixas por região
  ↓
┌─────────────────────────────┐
│ Head de Classificação       │ ← Qual classe?
│ Head de Bbox                │ ← Refinar posição?
│ Head de Máscara (FCN 14×14) │ ← Máscara dentro do bbox?
└─────────────────────────────┘
```

### Uso com Detectron2 ou torchvision

```python
import torchvision
from torchvision.models.detection import maskrcnn_resnet50_fpn

model = maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

with torch.no_grad():
    predictions = model([img_tensor])

masks = predictions[0]['masks']       # (N, 1, H, W)
labels = predictions[0]['labels']     # (N,) classes
scores = predictions[0]['scores']     # (N,) confiança

# Filtrar por confiança
threshold = 0.5
keep = scores > threshold
masks = masks[keep].squeeze(1)        # (N_filtered, H, W)
```

### Quando usar Mask R-CNN vs U-Net

| Cenário | Recomendação |
|---|---|
| Segmentar 1 tipo de objeto (ex: tumor) | U-Net |
| Segmentar múltiplos objetos distintos | Mask R-CNN |
| Precisa de ID único por instância | Mask R-CNN |
| Dataset pequeno (<1000 imagens) | U-Net com transfer learning |
| Dataset grande, precisão máxima | Mask R-CNN ou PointRend |

---

## 🧪 PROJETOS OBRIGATÓRIOS

### 1️⃣ Remoção de Fundo

* Segmentar objeto principal
* Aplicar máscara para remover fundo
* Substituir por fundo novo ou transparente (PNG com alpha)

### 2️⃣ U-Net do Zero

* Dataset simples (ex: Oxford Pets, Carvana, ou dataset próprio)
* Treino completo com BCE + Dice
* Avaliação: IoU e Dice por época (plotar curvas)
* Meta: IoU > 0.80

### 3️⃣ Segmentação Multi-Classe

* Pelo menos 3 classes + fundo
* Usar cross-entropy para multi-classe
* Avaliar mIoU (mean IoU sobre todas as classes)

### 4️⃣ Medição de Área

* Segmentar objeto
* Contar pixels da máscara
* Converter pixels para área real (se escala conhecida)

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Tipos de segmentação (semântica, instância, panóptica)
2. Representação de máscara (binária, multi-classe, one-hot)
3. Dataset imagem/máscara (estrutura + alinhamento)
4. Dataset PyTorch customizado com augmentation correto
5. Loss functions (BCE, Dice, Focal)
6. U-Net (implementar do zero)
7. Treinar U-Net em dataset simples
8. Visualização e debug de predições
9. Métricas: IoU, Dice, pixel accuracy
10. Pós-processamento morfológico
11. Mask R-CNN (uso, não implementação do zero)
12. **Projetos obrigatórios**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Não alinhar imagem e máscara (erros silenciosos devastadores)
* Aplicar flip na imagem mas não na máscara (destroi o treino)
* Não visualizar resultado intermediário durante treino
* Usar só pixel accuracy (inútil com classes desbalanceadas)
* Pular U-Net e ir direto para Mask R-CNN

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 09 se:

* [ ] Treina U-Net do zero com IoU > 0.80
* [ ] Entende pixel-level prediction (cada pixel tem gradiente)
* [ ] Avalia com IoU e Dice corretamente
* [ ] Aplica pós-processamento morfológico para melhorar máscara
* [ ] Segmenta múltiplos objetos de instâncias diferentes com Mask R-CNN
* [ ] Cria dataset próprio de segmentação com anotação manual


---

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


---

# FASE 10 — IA GENERATIVA 2D

> **Posição na trilha:** Primeira metade da Fase 9 original — split justificado pelo volume e pela diferença de carreira.
> **Nível:** Estado da Arte (Avançado/Pesquisa)
> **Tempo estimado:** 2–3 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 06 (Transformers + CLIP) e Fase 04 (PyTorch arquiteto)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### PyTorch Nível Arquiteto (Fases 04 e 05)

* Backpropagation customizado (saber onde o gradiente flui)
* Estruturas encoder-decoder (U-Net da Fase 08)
* Fluxo completo de treino, debug e avaliação

### Transformers e Atenção (Fase 06)

* Self-attention e cross-attention implementados
* Como texto guia imagem via cross-attention
* CLIP: embeddings de texto e imagem no mesmo espaço

### Probabilidade e Estatística (Fase 01)

* **CRÍTICO:** Distribuições normais, amostragem (sampling)
* Valor esperado, variância
* KL Divergence (Kullback-Leibler): entender a fórmula e a intuição

### 🚨 Aviso Importante

> Você **não vai treinar Stable Diffusion no seu PC**. Você vai:
> - Implementar versões miniatura para entender as arquiteturas
> - Fazer fine-tuning (LoRA) em modelos open-source
> - Usar HuggingFace Diffusers para inferência e customização
>
> Quem tenta treinar modelos fundacionais em casa perde semanas sem resultado.

---

## 🔹 BLOCO 1 — AUTOENCODERS CLÁSSICOS (PONTO DE PARTIDA)

### O que é um Autoencoder

```
Entrada (x)
    ↓ Encoder
Vetor Latente (z) — comprimido
    ↓ Decoder
Reconstrução (x̂) ≈ x
```

**Loss:** `L = ||x - x̂||²` (reconstrução pixel a pixel)

```python
class Autoencoder(nn.Module):
    def __init__(self, latent_dim=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 256), nn.ReLU(),
            nn.Linear(256, latent_dim)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256), nn.ReLU(),
            nn.Linear(256, 28*28), nn.Sigmoid(),
            nn.Unflatten(1, (1, 28, 28))
        )
    
    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)
```

### O Problema do Autoencoder para Geração

**Espaço latente "esburacado":**
* Pontos de treinamento mapeados para regiões isoladas
* Interpolação entre dois pontos gera imagens sem sentido
* Não serve para **gerar** imagens novas, só para **comprimir/reconstruir**

---

## 🔹 BLOCO 2 — VAE (VARIATIONAL AUTOENCODER)

> A grande sacada: em vez de mapear para um ponto fixo no espaço latente, mapear para uma **distribuição de probabilidade**.

### A Ideia Central

```
Autoencoder clássico:
  x → encoder → z (ponto fixo) → decoder → x̂

VAE:
  x → encoder → μ, σ (parâmetros de distribuição) → Sample z ~ N(μ, σ²) → decoder → x̂
```

### Reparameterization Trick (CRÍTICO)

**O problema:** `z ~ N(μ, σ²)` é uma operação estocástica — o gradiente não pode fluir através de "sortear um valor aleatório".

**A solução:** Separar o ruído do parâmetro aprendível:

```
z = μ + σ * ε,  onde ε ~ N(0, 1)
```

Agora o gradiente flui por `μ` e `σ` (parâmetros da rede) — `ε` é só ruído externo.

### Loss Function do VAE (Dois Termos)

```
L_VAE = L_reconstrução + β * L_KL

L_reconstrução = ||x - x̂||²  (ou BCE para pixels binários)

L_KL = -0.5 * Σ (1 + log(σ²) - μ² - σ²)
         Força distribuição latente → Normal padrão N(0, 1)
```

**Intuição do L_KL:** Evita que o encoder colapse para pontos isolados. Força o espaço latente a ser "organizado" — permite interpolação e geração.

### Implementação Completa

```python
class VAE(nn.Module):
    def __init__(self, latent_dim=64):
        super().__init__()
        
        # Encoder → μ e log_var (não σ — mais estável numericamente)
        self.encoder_shared = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU()
        )
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_log_var = nn.Linear(256, latent_dim)
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256), nn.ReLU(),
            nn.Linear(256, 512), nn.ReLU(),
            nn.Linear(512, 28*28), nn.Sigmoid(),
            nn.Unflatten(1, (1, 28, 28))
        )
    
    def encode(self, x):
        h = self.encoder_shared(x)
        return self.fc_mu(h), self.fc_log_var(h)
    
    def reparametrize(self, mu, log_var):
        # Reparameterization trick
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)  # N(0,1), mesmo shape que std
        return mu + std * eps
    
    def forward(self, x):
        mu, log_var = self.encode(x)
        z = self.reparametrize(mu, log_var)
        return self.decoder(z), mu, log_var

def vae_loss(reconstrucao, x, mu, log_var, beta=1.0):
    # Reconstrução (BCE)
    bce = F.binary_cross_entropy(reconstrucao, x, reduction='sum')
    # KL Divergence
    kl = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
    return bce + beta * kl
```

### Geração e Interpolação

```python
# Gerar imagem nova a partir de ruído
with torch.no_grad():
    z_novo = torch.randn(1, latent_dim)
    img_gerada = vae.decoder(z_novo)

# Interpolar entre duas imagens
z1 = vae.encode(img1)[0]  # μ de img1
z2 = vae.encode(img2)[0]  # μ de img2

for alpha in np.linspace(0, 1, 8):
    z_interp = (1 - alpha) * z1 + alpha * z2
    img_interp = vae.decoder(z_interp)
```

### 🚧 Exercício Obrigatório

* Implementar VAE para MNIST ou CelebA
* Gerar grade de imagens a partir de ruído aleatório
* Implementar interpolação entre duas imagens reais
* Visualizar o espaço latente 2D com t-SNE

---

## 🔹 BLOCO 3 — GANs (GENERATIVE ADVERSARIAL NETWORKS)

> O treino adversarial é um dos conceitos mais inteligentes e mais frustrantes em ML. A teoria é elegante. A prática é uma guerra de hiperparâmetros.

### A Dinâmica do Jogo (Minimax)

```
Generator (G): Noise z → Imagem Falsa
Discriminator (D): Imagem → Probabilidade [0=falsa, 1=real]

Objetivo do G: Enganar D (fazer D classificar falsa como 1)
Objetivo do D: Não ser enganado (classificar real=1, falsa=0)

Equilíbrio de Nash: G gera imagens tão boas que D fica em 50% (não consegue distinguir)
```

### Losses Formais

```python
# D quer maximizar: log D(x_real) + log(1 - D(G(z)))
# G quer minimizar: log(1 - D(G(z))) → equiv. maximizar log D(G(z))

criterio = nn.BCELoss()
reais = torch.ones(batch, 1)   # Labels: real = 1
falsos = torch.zeros(batch, 1) # Labels: falso = 0

# Treinar Discriminador
pred_real = D(imgs_reais)
pred_falso = D(G(z).detach())  # detach: não propagar para G aqui
loss_D = criterio(pred_real, reais) + criterio(pred_falso, falsos)

# Treinar Generator
pred_falso_g = D(G(z))
loss_G = criterio(pred_falso_g, reais)  # G quer que D classifique como real
```

### DCGAN (Deep Convolutional GAN)

```python
class Generator(nn.Module):
    def __init__(self, z_dim=100, img_channels=3, features=64):
        super().__init__()
        self.gen = nn.Sequential(
            # z_dim → 4×4
            self._block(z_dim, features*16, 4, 1, 0),        # 4×4
            self._block(features*16, features*8, 4, 2, 1),   # 8×8
            self._block(features*8, features*4, 4, 2, 1),    # 16×16
            self._block(features*4, features*2, 4, 2, 1),    # 32×32
            nn.ConvTranspose2d(features*2, img_channels, 4, 2, 1),  # 64×64
            nn.Tanh()  # [-1, 1] → normalização padrão de GAN
        )
    
    def _block(self, in_ch, out_ch, k, s, p):
        return nn.Sequential(
            nn.ConvTranspose2d(in_ch, out_ch, k, s, p, bias=False),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(True)
        )
    
    def forward(self, z):
        return self.gen(z.view(-1, z.shape[1], 1, 1))
```

### Problemas Críticos (O Inferno de Engenharia)

**Mode Collapse**
* G descobre 1 imagem que engana D e só gera ela repetidamente
* Sintoma: grade de imagens geradas todas iguais
* Soluções: Wasserstein Loss (WGAN), Label Smoothing, Unrolled GAN

**Vanishing Gradient**
* D fica tão bom que D(G(z)) → 0 → gradient de G desaparece
* G não aprende mais nada

**Instabilidade de Treino**
* Pequena mudança em lr → D domina G ou vice-versa → ciclo de colapso

### Boas Práticas para Estabilidade

```python
# 1. Usar LeakyReLU no Discriminador (não ReLU puro)
nn.LeakyReLU(0.2)

# 2. Label Smoothing (real = 0.9, não 1.0)
reais_suaves = 0.9 * torch.ones(batch, 1)

# 3. BatchNorm (exceto na 1ª camada do D e última do G)

# 4. Adam com lr=2e-4, betas=(0.5, 0.999) — padrão DCGAN

# 5. Treinar D mais vezes que G por step (ratio 1:2 ou 1:5)
for _ in range(n_critic):
    # Treinar D
    ...
# Treinar G uma vez
```

### 🚧 Projeto Obrigatório

* Treinar DCGAN para gerar imagens de animes, pokémons ou fashion-MNIST
* Monitorar loss de G e D ao longo do treino
* Documentar se ocorreu mode collapse e como você lidou

---

## 🔹 BLOCO 4 — MODELOS DE DIFUSÃO (CORAÇÃO DO ESTADO DA ARTE)

> DDPM (2020) + Latent Diffusion (2022) = Stable Diffusion. Entender isso é entender o que está por trás de Midjourney, DALL-E e Sora.

### A Física da Difusão

**Forward Process (Destruição controlada):**
```
x₀ (imagem limpa)
    ↓ adicionar ruído gaussiano gradualmente
x₁ (levemente ruidosa)
    ↓
x₂
    ↓ ...
x_T (ruído branco — não há mais informação da imagem)
```

```python
# Cronograma de ruído (noise schedule)
betas = torch.linspace(0.0001, 0.02, T)  # T=1000 timesteps
alphas = 1 - betas
alphas_cumprod = torch.cumprod(alphas, dim=0)

# Amostrar x_t diretamente a partir de x_0 (sem precisar de todos os passos)
def q_sample(x0, t, noise=None):
    if noise is None:
        noise = torch.randn_like(x0)
    sqrt_alpha = alphas_cumprod[t].sqrt().view(-1, 1, 1, 1)
    sqrt_one_minus = (1 - alphas_cumprod[t]).sqrt().view(-1, 1, 1, 1)
    return sqrt_alpha * x0 + sqrt_one_minus * noise
```

**Reverse Process (O modelo aprende a desfazer):**

A rede neural **não aprende a imagem diretamente**. Ela aprende a **prever o ruído** que foi adicionado:

```
U-Net(x_t, t) → ε_pred (ruído estimado)
Loss = ||ε - ε_pred||²   (onde ε é o ruído real que foi adicionado)
```

### Implementação Simplificada (Toy DDPM)

```python
class ToyDDPM(nn.Module):
    """U-Net simplificada para dados de baixa resolução."""
    def __init__(self, channels=1, time_emb_dim=32):
        super().__init__()
        # Embedding do timestep (o modelo precisa saber em qual step está)
        self.time_mlp = nn.Sequential(
            SinusoidalPositionEmbs(time_emb_dim),
            nn.Linear(time_emb_dim, time_emb_dim*4),
            nn.GELU(),
        )
        # Arquitetura U-Net modificada (aceita timestep)
        # ... (simplificado para legibilidade)
    
    def forward(self, x, t):
        """
        x: imagem ruidosa (batch, channels, H, W)
        t: timestep (batch,) — qual passo da difusão
        Retorna: ruído estimado ε_pred
        """
        t_emb = self.time_mlp(t)
        # ... processar x condicionado em t_emb
        return ruido_estimado

# Loop de treino
for batch in loader:
    x0 = batch  # Imagens limpas
    t = torch.randint(0, T, (batch_size,))  # Timestep aleatório
    noise = torch.randn_like(x0)
    x_t = q_sample(x0, t, noise)  # Imagem ruidosa no timestep t
    
    predicted_noise = model(x_t, t)
    loss = F.mse_loss(predicted_noise, noise)  # Comparar ruído predito com real
    
    optimizer.zero_grad(); loss.backward(); optimizer.step()
```

### Sampling (Geração)

```python
@torch.no_grad()
def p_sample_loop(model, shape):
    """Gerar imagem partindo de ruído puro."""
    img = torch.randn(*shape)  # x_T: ruído puro
    
    for t in reversed(range(0, T)):
        t_batch = torch.full((shape[0],), t)
        predicted_noise = model(img, t_batch)
        
        # Fórmula de DDPM para x_{t-1} dado x_t e ε_pred
        alpha = alphas[t]
        alpha_bar = alphas_cumprod[t]
        beta = betas[t]
        
        img = (1 / alpha.sqrt()) * (img - beta / (1 - alpha_bar).sqrt() * predicted_noise)
        
        if t > 0:  # Adicionar ruído exceto no último passo
            img += beta.sqrt() * torch.randn_like(img)
    
    return img.clamp(-1, 1)
```

### Latent Diffusion (O que torna tudo rápido)

**Problema:** Rodar difusão em imagem 512×512 é computacionalmente insuportável (1000 passos × 3 × 512 × 512).

**Solução em 2 etapas:**

```
1. VAE Encoder:   x (512×512×3) → z (64×64×4)     ← 48x menor!
2. Difusão:       Rodar DDPM no espaço latente z    ← muito mais rápido
3. VAE Decoder:   z̃ (64×64×4) → x̂ (512×512×3)    ← reconstruir
```

**Cross-Attention para guiar com texto:**
```
CLIP Text Encoder → embeddings de texto
    ↓
Injetar em cada camada da U-Net via cross-attention
    ↓
U-Net agora sabe "para onde" denoisar
```

### Fine-Tuning com LoRA

```python
# LoRA: treinar só matrizes de baixo rank — 99% menor que treinar tudo
from diffusers import StableDiffusionPipeline
from peft import get_peft_model, LoraConfig

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Aplicar LoRA só nas camadas de atenção
lora_config = LoraConfig(
    r=4,                    # Rank (baixo = menos parâmetros)
    lora_alpha=32,
    target_modules=["to_k", "to_q", "to_v", "to_out.0"],
    lora_dropout=0.1
)
pipe.unet = get_peft_model(pipe.unet, lora_config)
```

### 🚧 Mini-projeto Obrigatório

* Implementar Toy DDPM para dados 2D simples ou MNIST
* Visualizar: processo de destruição (x₀ → x_T) e geração (x_T → x₀)
* Bonus: Fine-tune Stable Diffusion com LoRA em estilo artístico

---

## 🔹 BLOCO 5 — MANIPULAÇÃO NO ESPAÇO LATENTE

> Com VAE e Diffusion treinados, o espaço latente tem estrutura semântica. Você pode navegar nele.

### Interpolação Latente com VAEs

```python
# Transição suave entre dois rostos
z1 = encoder(rosto_triste)
z2 = encoder(rosto_feliz)

imagens_transicao = []
for alpha in np.linspace(0, 1, 10):
    z_interp = (1 - alpha) * z1 + alpha * z2
    img = decoder(z_interp)
    imagens_transicao.append(img)
```

### Aritmética Latente (como word2vec de imagens)

```python
# "Homem com óculos" - "Homem" + "Mulher" = "Mulher com óculos"
z_homem_oculos = encoder(img_homem_oculos)
z_homem = encoder(img_homem)
z_mulher = encoder(img_mulher)

z_resultado = z_homem_oculos - z_homem + z_mulher
img_resultado = decoder(z_resultado)
```

### 🚧 Projeto Obrigatório

* Treinar VAE em dataset de faces (CelebA subset)
* Encontrar vetores de atributo: `v_sorriso`, `v_oculos`, `v_barba`
* Aplicar e remover atributos matematicamente

---

## 🧪 PROJETOS OBRIGATÓRIOS DE PORTFÓLIO

### 1️⃣ Seu Próprio Mini "Midjourney"

* Implementar DDPM do zero
* Treinar em dataset temático pequeno (sprites de jogos, ícones, emojis, fashion)
* Interface: digitar descrição → gerar imagem (LoRA em SD ou toy model)
* **Meta:** Demonstrar geração de imagens novas coerentes com o dataset

### 2️⃣ Sistema de Interpolação Visual

* Treinar VAE ou usar embeddings CLIP
* Interface: enviar 2 imagens → gerar 8 frames de transição entre elas
* Demonstrar aritmética latente: A - B + C = D

### 3️⃣ Fine-Tuning com LoRA

* Escolher estilo artístico (pintura a óleo, anime, pixel art)
* Fine-tunar Stable Diffusion com LoRA em 20-50 imagens do estilo
* Comparar: prompts com e sem o estilo treinado

### 4️⃣ Análise Comparativa

* Comparar 3 abordagens para o mesmo dataset:
  * Autoencoder → reconstuição pura
  * VAE → geração com interpolação
  * DCGAN → geração adversarial
* Documentar qualidade visual, modo de colapso, dificuldade de treino

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Autoencoders clássicos (implementar + treinar)
2. Problema do espaço latente "esburacado"
3. VAE: reparameterization trick
4. Loss VAE (reconstrução + KL)
5. Interpolação e aritmética latente com VAE
6. GAN: dinâmica do jogo (teoria)
7. DCGAN (implementar do zero)
8. Problemas: mode collapse, gradients vanishing
9. Técnicas de estabilização
10. DDPM: forward process (adicionar ruído)
11. DDPM: reverse process (prever ruído)
12. Toy DDPM (implementar e treinar)
13. Latent Diffusion (conceito + uso HuggingFace)
14. Fine-tuning com LoRA
15. **Projetos de portfólio**

---

## 🚨 ERROS FATAIS NESTA FASE

* Tentar treinar Stable Diffusion do zero no PC — impossível sem cluster de GPU
* Usar WebUIs (ComfyUI, A1111) sem entender o código por baixo
* Pular implementação manual do VAE e DDPM
* Ignorar mode collapse — debugar é parte do aprendizado
* Não visualizar o espaço latente (o principal insight desta fase é a estrutura semântica)

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 11 se:

* [ ] Explica Reparameterization Trick no quadro branco sem consultar nada
* [ ] Implementa e treina VAE com interpolação funcional
* [ ] Treina DCGAN sem mode collapse imediato (estabiliza o treino)
* [ ] Implementa DDPM toy (forward + reverse) e gera imagens
* [ ] Entende como cross-attention conecta texto a pixels em SD
* [ ] Fine-tuna Stable Diffusion com LoRA em estilo próprio


---

# FASE 11 — VISÃO 3D E NEURAL RENDERING

> **Posição na trilha:** Segunda metade da Fase 9 original — trilha de carreira independente (Visão 3D, SLAM, Robótica, XR).
> **Nível:** Estado da Arte (Pesquisa aplicada)
> **Tempo estimado:** 2–3 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 04 (PyTorch sólido), Fase 05 (CNNs), Fase 08 (segmentação — para U-Net conceito)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Matemática (Fase 01 — mas agora 3D)

* **Álgebra Linear Espacial (CRÍTICO):**
  * Matrizes de rotação e translação
  * Homogeneous coordinates (coordenadas homogêneas)
  * Produto de matrizes de transformação

### PyTorch

* Implementar MLP customizado
* Custom loss functions
* Gradiente fluindo por operações não-triviais

### Visão Computacional Clássica (Fase 03)

* Manipulação de imagem
* Coordenadas de pixel

---

## 🔹 BLOCO 1 — MATEMÁTICA DA CÂMERA 3D (BASE ABSOLUTA)

> Sem isso, NeRF e Gaussian Splatting são magia incompreensível. Com isso, são engenharia.

### Por que a câmera importa?

Toda reconstrução 3D parte desta pergunta: "Como um ponto (X, Y, Z) no mundo vira o pixel (u, v) na tela?"

### Coordenadas Homogêneas

```
Ponto 3D no mundo:  P_w = [X, Y, Z, 1]ᵀ   (4D com 1 no final)
Ponto 2D na imagem: p = [u, v, 1]ᵀ        (3D com 1 no final — homogêneo)
```

Por que adicionar 1? Permite representar translação como multiplicação de matriz — elegância matemática.

### Câmera Extrínseca [R | t] — Onde a Câmera Está no Mundo

```
        [R₃ₓ₃ | t₃ₓ₁]
[R|t] = [             ]  ← 3×4
        
R: Matriz de rotação 3×3 (orientação da câmera)
t: Vetor de translação 3×1 (posição da câmera)
```

**Transformar ponto do mundo para câmera:**
```python
# P_camera = R @ P_world + t
P_camera = R @ P_world + t
```

**Interpretação:** Se você mover a câmera 1m para direita, `t` muda. Se você girar a câmera 30° para esquerda, `R` muda.

### Câmera Intrínseca K — A Lente

```
    [fx  0   cx]
K = [0   fy  cy]    ← 3×3
    [0   0    1]

fx, fy: Focal length em pixels (quanto a câmera "amplia")
cx, cy: Centro óptico da imagem (normalmente W/2, H/2)
```

### Projeção Completa (Pinhole Model)

```python
def projetar_ponto_3d(P_world, R, t, K):
    """
    P_world: ponto 3D no mundo (3,)
    R: matriz de rotação (3,3)
    t: translação (3,)
    K: intrínsecos (3,3)
    Retorna: ponto 2D na imagem (u, v)
    """
    # 1. Mundo → Câmera
    P_cam = R @ P_world + t    # (3,)
    
    # 2. Câmera → Imagem (projeção perspectiva)
    P_img_hom = K @ P_cam      # (3,)
    
    # 3. Normalizar coordenadas homogêneas
    u = P_img_hom[0] / P_img_hom[2]
    v = P_img_hom[1] / P_img_hom[2]
    
    return u, v
```

### 🚧 Exercício Fundamental

* Criar cena 3D simples (cubo de pontos)
* Projetar de 4 ângulos diferentes (variando R e t)
* Verificar que projeção corresponde ao que você esperaria visualmente

---

## 🔹 BLOCO 2 — REPRESENTAÇÕES 3D

> Antes de aprender modelos 3D neurais, entender as representações clássicas.

### Point Clouds (Nuvens de Pontos)

```python
import numpy as np
import open3d as o3d

# Array Nx3 (N pontos, cada um com X, Y, Z)
pontos = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], ...])

# Visualizar com Open3D
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pontos)
o3d.visualization.draw_geometries([pcd])
```

**Vantagens:** Simples, diretamente de LiDAR e câmeras de profundidade  
**Desvantagens:** Esparsa, sem superfície explícita

### Voxel Grids

```
3D grid de células (como pixels mas 3D)
Resolução 64³ → 262.144 células
Resolução 256³ → 16.777.216 células   ← memória explode
```

**Problema:** `O(N³)` — inviável em alta resolução

### Meshes (Malhas 3D)

```python
# Vértices + Faces (triângulos)
vertices = [[0,0,0], [1,0,0], [0,1,0], [0,0,1]]  # 4 vértices
faces = [[0,1,2], [0,1,3], [0,2,3], [1,2,3]]      # 4 triângulos

mesh = o3d.geometry.TriangleMesh()
mesh.vertices = o3d.utility.Vector3dVector(vertices)
mesh.triangles = o3d.utility.Vector3iVector(faces)
```

**Padrão da indústria:** jogos, animação, manufatura  
**Problema:** Difícil de reconstruir automaticamente de fotos

### Representações Neurais (Implícitas)

* A cena 3D é codificada nos **pesos de uma rede neural** — não em arquivo .obj
* Consulta: "Qual a cor/densidade deste ponto (x,y,z)?"
* Resposta: rodar o MLP naquelas coordenadas

---

## 🔹 BLOCO 3 — ESTIMATIVA DE PROFUNDIDADE

### Visão Estéreo

```
Câmera Esquerda  |  Câmera Direita
     ────────────────────────
                    d (disparidade)
     
Profundidade Z = f * B / d
onde:
  f = focal length
  B = baseline (distância entre câmeras)
  d = disparidade em pixels (objeto longe → disparidade pequena)
```

**Como os humanos veem em 3D:** Exatamente o mesmo princípio — dois olhos separados horizontalmente.

```python
import cv2

# Computar disparidade com OpenCV
stereo = cv2.StereoBM.create(numDisparities=96, blockSize=15)
disparity = stereo.compute(img_left, img_right)

# Converter disparidade → profundidade
depth = (focal * baseline) / (disparity + 1e-6)
```

### Monocular Depth Estimation (Uma só câmera)

```python
from transformers import pipeline

# MiDaS ou DepthAnything — estado da arte
depth_estimator = pipeline("depth-estimation", model="depth-anything/Depth-Anything-V2-Small")

img = Image.open("foto.jpg")
resultado = depth_estimator(img)
mapa_profundidade = resultado['predicted_depth']  # Valores relativos

# Visualizar
plt.imshow(mapa_profundidade, cmap='plasma')
plt.colorbar(label='Profundidade (relativa)')
```

### Criar Point Cloud a partir de Depth Map

```python
def depth_to_pointcloud(depth_map, K):
    """
    depth_map: (H, W) mapa de profundidade
    K: matrix intrínseca (3,3)
    Retorna: (N, 3) nuvem de pontos
    """
    H, W = depth_map.shape
    fx, fy = K[0,0], K[1,1]
    cx, cy = K[0,2], K[1,2]
    
    u, v = np.meshgrid(np.arange(W), np.arange(H))
    z = depth_map
    x = (u - cx) * z / fx
    y = (v - cy) * z / fy
    
    pontos = np.stack([x, y, z], axis=-1).reshape(-1, 3)
    return pontos[pontos[:, 2] > 0]  # Remover pontos inválidos
```

### 🚧 Exercício

1. Tirar foto de objeto na mesa
2. Rodar DepthAnything
3. Converter mapa de profundidade em point cloud 3D
4. Visualizar no Open3D

---

## 🔹 BLOCO 4 — COLMAP E STRUCTURE FROM MOTION

> COLMAP é o padrão da indústria para extrair geometria 3D de fotos comuns.

### Structure from Motion (SfM): Intuição

**Problema:** Tenho 100 fotos do mesmo objeto. Onde cada câmera estava?  
**Solução:** Encontrar pontos comuns entre fotos → triangular posição 3D → resolver posição das câmeras.

```
Fotos de múltiplos ângulos
    ↓
SIFT / SuperPoint → Features em cada imagem
    ↓
Feature Matching → Quais features são o mesmo ponto 3D?
    ↓
RANSAC + Triangulação → Posição 3D dos pontos
    ↓
Bundle Adjustment → Otimizar cameras + pontos simultaneamente
    ↓
Saída: Matrizes R, t de cada câmera + sparse point cloud
```

### Usar COLMAP na Prática

```bash
# Instalar COLMAP (Windows: colmap.github.io)

# 1. Estrutura de pastas
mkdir meu_objeto
mkdir meu_objeto/images

# 2. Colocar imagens em meu_objeto/images/

# 3. Rodar pipeline automático
colmap automatic_reconstructor \
    --workspace_path meu_objeto/ \
    --image_path meu_objeto/images/

# Saída:
# meu_objeto/sparse/0/cameras.bin   ← Intrínsecos K por câmera
# meu_objeto/sparse/0/images.bin    ← Extrínsecos R,t por imagem
# meu_objeto/sparse/0/points3D.bin  ← Sparse point cloud
```

### Ler Saída do COLMAP em Python

```python
import pycolmap

rec = pycolmap.Reconstruction("meu_objeto/sparse/0")

for img_id, img in rec.images.items():
    R = img.rotation_matrix()   # 3×3
    t = img.tvec                # 3,
    print(f"Câmera {img.name}: posição aproximada {-R.T @ t}")

# Exportar point cloud
points = np.array([p.xyz for p in rec.points3D.values()])
print(f"Pontos 3D: {points.shape}")
```

---

## 🔹 BLOCO 5 — NeRF (NEURAL RADIANCE FIELDS)

> NeRF revolucionou reconstrução 3D em 2020. A cena inteira vive dentro dos pesos de um MLP.

### Como Funciona

```
Entrada do MLP:
  (x, y, z)      ← Ponto 3D no espaço
  (θ, φ)          ← Ângulo de visão (direção do raio)

Saída do MLP:
  (R, G, B)       ← Cor daquele ponto naquele ângulo
  σ               ← Densidade (quão sólido está o ponto)
```

### Volume Rendering (A Magia)

Para gerar um pixel: disparar raio da câmera através da cena, amostrar N pontos ao longo do raio, acumular cores e densidades:

```python
def volume_render(colors, sigmas, deltas):
    """
    colors: (N, 3) — cor de cada ponto amostrado
    sigmas: (N,)   — densidade de cada ponto
    deltas: (N,)   — distância entre pontos consecutivos
    Retorna: cor final do pixel (3,)
    """
    # Transmitância: quanto de luz "passou" até este ponto
    alpha = 1 - torch.exp(-sigmas * deltas)
    
    # Produto cumulativo de transparências anteriores
    transmitancia = torch.cumprod(
        torch.cat([torch.ones((1,)), 1 - alpha[:-1]]), dim=0
    )
    
    # Pesos: contribuição de cada ponto para o pixel
    pesos = alpha * transmitancia  # (N,)
    
    # Cor final: soma ponderada
    cor_pixel = (pesos[:, None] * colors).sum(dim=0)  # (3,)
    
    return cor_pixel
```

### Loss do NeRF

```python
# Simples: comparar cor renderizada com cor real do pixel
loss = F.mse_loss(cor_renderizada, cor_pixel_real)
```

**O modelo aprende:** Ajustar os pesos do MLP para que, ao renderizar de qualquer ângulo, a imagem gerada bata com as fotos reais. Depois de treinado, pode gerar de **qualquer ângulo nunca visto**.

### Implementação Mínima

```python
class NeRFMLP(nn.Module):
    def __init__(self, pos_enc_dim=10, dir_enc_dim=4):
        super().__init__()
        # Positional encoding aumenta dimensionalidade para capturar detalhes finos
        in_dim = 3 + 3*2*pos_enc_dim  # xyz + senos/cossenos
        
        self.net = nn.Sequential(
            nn.Linear(in_dim, 256), nn.ReLU(),
            nn.Linear(256, 256), nn.ReLU(),
            nn.Linear(256, 256), nn.ReLU(),
            nn.Linear(256, 256), nn.ReLU(),
        )
        self.sigma_head = nn.Linear(256, 1)  # Densidade
        self.color_head = nn.Linear(256 + 3*2*dir_enc_dim, 128)  # Cor (depende do ângulo)
        self.color_out = nn.Sequential(nn.Linear(128, 3), nn.Sigmoid())
    
    def positional_encoding(self, x, num_freqs):
        encodings = [x]
        for i in range(num_freqs):
            encodings += [torch.sin(2**i * x), torch.cos(2**i * x)]
        return torch.cat(encodings, dim=-1)
    
    def forward(self, xyz, dirs):
        xyz_enc = self.positional_encoding(xyz, self.pos_enc_dim)
        h = self.net(xyz_enc)
        sigma = F.relu(self.sigma_head(h))
        
        dir_enc = self.positional_encoding(dirs, self.dir_enc_dim)
        color = self.color_out(self.color_head(torch.cat([h, dir_enc], -1)))
        
        return sigma, color
```

### Limitações do NeRF

| Limitação | Impacto |
|---|---|
| Treino lento (horas-dias) | Inviável para aplicações em tempo real |
| Inferência lenta (1+ min/frame) | Não serve para visualização interativa |
| Uma cena por modelo | Não generaliza para novas cenas sem retreinar |
| Qualidade em regiões não vistas | Incerta — só interpola, não extrapola bem |

### Implementação Prática

```bash
# Usar nerfstudio — implementação otimizada moderna
pip install nerfstudio

# Preparar dados com COLMAP
ns-process-data images --data meu_objeto/images/ --output-dir dados_nerf/

# Treinar NeRF
ns-train nerfacto --data dados_nerf/

# Renderizar vídeo de 360°
ns-render camera-path --load-config outputs/...
```

---

## 🔹 BLOCO 6 — 3D GAUSSIAN SPLATTING (ESTADO DA ARTE ATUAL)

> Lançado em 2023. Superou o NeRF em velocidade por 100x+ mantendo qualidade superior. É o que as empresas de XR, metaverso e reconstrução 3D estão usando agora.

### O Conceito

**Em vez de um MLP pesado, representar a cena como milhões de "bolinhas" (Gaussianas 3D):**

```
Cada Gaussiana tem:
  μ         ← Posição (X, Y, Z) no espaço
  Σ         ← Covariância 3×3 (formato: esférica, achatada, alongada)
  α         ← Opacidade (transparente a sólida)
  SH        ← Spherical Harmonics para cor dependente do ângulo de visão
```

**Splatting:** Para renderizar uma imagem, "espalhar" (splat) cada Gaussiana na câmera 2D e acumular as contribuições — é uma operação muito eficiente na GPU.

### Por que é Rápido?

* NeRF: Para cada pixel, rodar MLP em N pontos = N forward passes
* GS: Rasterizar Gaussianas ordenadas por profundidade = operação GPU paralela

**Resultado:** 100+ FPS de renderização interativa (vs NeRF que levava minutos)

### Treinamento

```
1. Sparse point cloud (COLMAP) → Inicializar Gaussianas em cada ponto
2. Para cada imagem de treino:
   a. Renderizar cena com Gaussianas atuais
   b. Comparar com foto real (L1 loss + SSIM loss)
   c. Propagar gradiente → ajustar posição, forma, cor, opacidade
3. Densificar: adicionar Gaussianas em regiões com gradiente alto
4. Podar: remover Gaussianas transparentes ou muito grandes
```

### Uso Prático (gsplat / 3D Gaussian Splatting)

```bash
# Instalar
pip install gsplat

# Treinar (após ter saída do COLMAP)
python train.py -s meu_objeto/ -m saida_gaussians/

# Visualizar interativo (WebGL)
python render.py -m saida_gaussians/ --web
```

### Resultado Esperado

* Objeto simples (caixa, estátua): 20-40 min de treino, qualidade foto-realista
* Quarto/ambiente: 1-3h de treino
* Visualização interativa a 100+ FPS no browser

---

## 🔹 BLOCO 7 — GERAÇÃO 3D (FRONTEIRA ATUAL)

> Esta área está evoluindo rapidamente. O objetivo é entender os princípios — as ferramentas mudam a cada 6 meses.

### Text-to-3D (Score Distillation Sampling — SDS)

```
Prompt de texto → ?→ Modelo 3D

Como funciona:
1. Inicializar modelo 3D (NeRF ou Gaussianas) como borrão
2. Renderizar de ângulo aleatório → imagem 2D
3. Passar essa imagem por Stable Diffusion congelado
4. SD julga: "o quanto isso parece com o prompt?"
5. Gradiente de SD → volta para o modelo 3D → ajusta Gaussianas
6. Repetir de vários ângulos
```

**Exemplo de ferramentas:** DreamFusion (Google), MVDream, Wonder3D

### Image-to-3D

```
1 foto → Modelo 3D completo

Como funciona:
- Rede treinada em milhões de pares (foto, modelo 3D)
- Aprende a "alucidar" o que há atrás e embaixo do objeto
```

**Ferramentas:** Zero123, LRM, InstantMesh (state of art em 2024)

```python
# Uso típico com InstantMesh
from huggingface_hub import hf_hub_download

# Uma foto de entrada → reconstrução 3D em segundos
pipe = InstantMeshPipeline.from_pretrained("TencentARC/InstantMesh")
meshes = pipe("foto_objeto.png")
meshes[0].export("objeto_3d.obj")
```

---

## 🧪 PROJETOS OBRIGATÓRIOS (PORTFÓLIO PESADO)

### 1️⃣ Fotogrametria para Nuvem de Pontos 3D

**Objetivo:** Reconstruir objeto da mesa em 3D com câmera de celular

1. Gravar vídeo do objeto (30-60 segundos, dar a volta completa)
2. Extrair frames: `ffmpeg -i video.mp4 -vf fps=2 frames/frame_%04d.jpg`
3. Rodar COLMAP para obter poses das câmeras + sparse cloud
4. Visualizar nuvem de pontos esparsa no Open3D
5. Aplicar DepthAnything para dense depth + criar nuvem densa

### 2️⃣ Seu Quarto em 3D Gaussian Splatting

**Objetivo:** Criar modelo 3D fotorrealista navegável em tempo real

1. Usar saída do projeto anterior (COLMAP)
2. Treinar Gaussian Splatting
3. Exportar visualizador WebGL (rodar no browser)
4. Navegar pelo modelo 3D do quarto em tempo real

### 3️⃣ Depth Estimation Pipeline

**Objetivo:** Sistema que recebe imagem e retorna:
* Mapa de profundidade colorido (DepthAnything)
* Nuvem de pontos 3D interativa (Open3D)
* Segmentação 3D do objeto principal (combinar com SAM ou Fase 08)

### 4️⃣ Reconstrução de Objeto de Produto

**Objetivo:** Recriar produto (sapato, boneco, caixa) para e-commerce 3D

1. Fotografar objeto em plataforma giratória (ou à mão, dando a volta)
2. COLMAP → poses
3. 3D Gaussian Splatting → modelo fotorrealista
4. Exportar como arquivo visualizável (.ply ou WebGL)

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Coordenadas homogêneas e produto de matrizes
2. Modelo de câmera: intrínseca K + extrínseca [R|t]
3. Projeção de ponto 3D → pixel 2D (implementar)
4. Representações 3D: point cloud, voxel, mesh
5. Visão estéreo: disparidade → profundidade
6. DepthAnything: depth de imagem única
7. Depth map → point cloud (implementar)
8. COLMAP: SfM na prática (seu objeto)
9. ler poses COLMAP em Python
10. Volume Rendering (implementar manual)
11. NeRF: implementar toy MLP
12. NeRF com nerfstudio (objeto real)
13. 3D Gaussian Splatting (objeto real)
14. Visualizador WebGL interativo
15. Geração 3D (conceito + ferramentas)
16. **Projetos de portfólio**

---

## 🚨 ERROS FATAIS NESTA FASE

* Ignorar a matemática da câmera (NeRF e GS viram caixa-preta sem isso)
* Não usar COLMAP antes de NeRF/GS (poses das câmeras são entrada obrigatória)
* Tentar treinar Text-to-3D no PC sem GPU potente — não funciona
* Não visualizar resultados intermediários (nuvem de pontos, poses)

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 12 se:

* [ ] Implementa projeção 3D → 2D matematicamente (código + visualização)
* [ ] Usa COLMAP para extrair poses de câmera de fotos reais
* [ ] Entende volume rendering e como o gradiente flui pelo NeRF
* [ ] Constrói model 3D fotorrealista com GS e visualiza em tempo real
* [ ] Cria pipeline depth → point cloud → visualização 3D interativa


---

# FASE 12 — PORTFÓLIO E CARREIRA

> **Posição na trilha:** Fase final. Transforma o que você construiu em posicionamento profissional.
> **Nível:** Profissional (estratégia de carreira)
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Quando começar:** Assim que tiver o projeto da Fase 07 (Object Detection) funcionando — não espere acabar tudo

---

## ⚠️ POR QUE ESTA FASE EXISTE

O erro mais comum de quem termina um roadmap técnico extenso:

> "Aprendi muito, mas não consigo me posicionar, não tenho portfólio apresentável e não sei como entrar no mercado."

Esta fase resolve isso sistematicamente. **Não é opcional.**

---

## 🔹 BLOCO 1 — O QUE CONTA COMO PORTFÓLIO

### O que NÃO é portfólio

* "Segui o tutorial do MNIST com 99% accuracy" — Todo mundo tem isso
* "Implementei a U-Net do paper" — Todo mundo que chegou até aqui tem isso
* "Notebook Jupyter com células de código e alguns prints"

### O que É portfólio

* Projeto com **problema real** → você coletou os dados, treinou, avaliou, deployou
* Produto funcional que outra pessoa pode usar (API, app, demo web)
* Solução que resolve algo que você mesmo precisou resolver
* Benchmark/comparação original que gera insight não óbvio

### A Regra de Ouro

**Cada projeto de portfólio deve ter um usuário hipotético que se beneficiaria dele.**

Não: "Treinei YOLO"  
Sim: "Sistema que detecta EPIs em imagens de construção — pode ser usado por apps de segurança do trabalho"

---

## 🔹 BLOCO 2 — SELEÇÃO E MATURAÇÃO DOS PROJETOS

### Quais Projetos Elevar ao Portfólio

**Selecione 3–5 projetos** das fases anteriores que você vai **elevar** — não é criar do zero, é completar e apresentar bem.

**Critérios de seleção:**

| Critério | Peso |
|---|---|
| Problema real (não só exercício acadêmico) | Alto |
| Dataset próprio (você coletou) | Alto |
| Deploy funcional (outra pessoa pode usar) | Alto |
| Resultado mensurável (mAP, accuracy, latência) | Médio |
| Código bem escrito (não notebook bagunçado) | Médio |
| Área que você quer trabalhar | Alto |

### Elevação de Projeto: Checklist

Para cada projeto de portfólio, fazer:

**[ ] Problema claro**
* "Este sistema resolve X para quem tem Y problema"
* Não: "Implementação de YOLO para detecção"
* Sim: "Monitor de segurança em construção: detecta ausência de capacete e emite alerta"

**[ ] Dataset próprio ou com contribuição original**
* Coletar imagens com câmera própria (webcam, celular)
* Ou: usar dataset público MAS adicionar algo original (novas classes, novo split, benchmark)

**[ ] Código limpo e estruturado**
```
projeto/
├── README.md          ← Documentação central (ver Bloco 3)
├── requirements.txt
├── data/
├── src/
│   ├── train.py
│   ├── evaluate.py
│   └── inference.py
├── notebooks/
│   └── exploratory.ipynb
├── models/            ← Pesos do modelo (ou link DVC)
└── demo/              ← Interface ou script de demo
```

**[ ] Métricas documentadas**
* Não: "funciona bem"
* Sim: "mAP@0.5 = 0.87 no conjunto de validação (200 imagens), latência = 23ms em RTX 3060"

**[ ] Demo funcional**
* Streamlit, Gradio, ou API com Swagger (`/docs`)

**[ ] Repositório GitHub com commit history limpo**
* Não commitar modelo .pth (usar DVC ou HuggingFace Hub)
* README com badges de métricas

---

## 🔹 BLOCO 3 — README PERFEITO (TEMPLATE)

```markdown
# [Nome do Projeto] 🔍

> **Uma frase descrevendo o que faz e para quem é útil.**

[Badge CI] [Badge Python] [Badge License]

## Demonstração

![demo.gif](demo.gif)   ← GIF de 10-30s mostrando funcionando

## Problema

[Descrever o problema real. Por que ele importa? Quem tem esse problema?]

## Solução

[Como seu sistema resolve o problema. Qual modelo? Qual abordagem?]

## Métricas

| Métrica | Valor |
|---|---|
| mAP@0.5 | 0.87 |
| Latência (GPU) | 23ms |
| Latência (CPU) | 180ms |
| Dataset | 1.200 imagens / 3 classes |

## Instalação e Uso

\`\`\`bash
git clone https://github.com/seu-usuario/projeto.git
cd projeto
pip install -r requirements.txt

# Demo
python demo.py --source webcam
\`\`\`

## Estrutura do Projeto

[Descrever src/, data/, models/]

## Como Treinei

[Resumo: dataset, tempo de treino, ambiente, decisões técnicas]

## Limitações Conhecidas

[O que o sistema não faz bem. Honestidade = credibilidade]

## Próximos Passos

[O que você faria com mais tempo]
```

---

## 🔹 BLOCO 4 — GITHUB: PRESENÇA PROFISSIONAL

### Profile README

Criar arquivo `github.com/seu-usuario/seu-usuario/README.md`:

```markdown
# Olá, sou [Nome] 👋

Engenheiro de Visão Computacional e IA com foco em sistemas de detecção e segmentação.

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv)

## Projetos em Destaque

| Projeto | Descrição | Métricas |
|---|---|---|
| [Monitor EPI](link) | Detecção de equipamentos de segurança | mAP 0.87 |
| [Análise de Células](link) | Segmentação de imagens médicas | Dice 0.92 |
| [Buscador Visual](link) | CLIP para busca semântica de imagens | — |
```

### Estratégia de Commits

* Commits pequenos e descritivos: "Add Dice loss implementation" não "update"
* Manter repositórios públicos limpos (sem "teste", "temp", "lixo" nos commits)
* Usar releases para versões estáveis: `v1.0.0-alpha`

### HuggingFace Hub

* Publicar modelos treinados no HuggingFace: `model.push_to_hub("seu-usuario/detector-epi")`
* HuggingFace tem inference API gratuita — demo instantâneo

---

## 🔹 BLOCO 5 — LINKEDIN E POSICIONAMENTO

### Headline (não deixar o padrão)

**Ruim:** "Estudante de Ciência da Computação"  
**Melhor:** "Engenheiro de Visão Computacional | PyTorch · YOLO · Segmentação"  
**Melhor ainda:** "Visão Computacional para Segurança Industrial | Detecção de EPIs em Tempo Real"

### Seção "Sobre"

```
Especialista em sistemas de visão computacional com foco em detecção e 
segmentação de objetos aplicados a [área que você quer].

Construí sistemas que [resultado concreto]:
→ Detector de EPIs com mAP 0.87, rodando a 30fps em câmeras IP
→ Pipeline de segmentação de células com Dice score 0.92
→ API de visão containerizada em Docker, servindo 500 req/min

Stack: Python · PyTorch · OpenCV · YOLO · FastAPI · Docker · CUDA
```

### Posts de Aprendizado

Durante o roadmap, publicar **1 post por semana** no LinkedIn sobre o que aprendeu:

* "Entendi hoje por que skip connections da U-Net funcionam — aqui a intuição em 5 pontos"
* "Testei 3 loss functions diferentes para segmentação de células — qual ganhou?"
* "Meu modelo de detecção de capacetes chegou em mAP 0.87 — aqui o que mais ajudou"

**Por que isso funciona:** Recrutadores buscam pessoas que **ensinam**, não só estudam. Post com imagem > post só com texto.

---

## 🔹 BLOCO 6 — PROJETOS DE PORTFÓLIO RECOMENDADOS

Escolha **1 por setor** de interesse:

### Segurança e Industria

* Detector de EPIs (capacete, colete, óculos) em câmeras IP
* Inspeção de qualidade de produto (defeitos na linha de produção)
* Detector de risco em canteiro (pessoa em área proibida)

### Saúde e Medicina

* Segmentação de células em microscópio
* Detecção de objetos em raio-X
* Análise de lesões dermatológicas

### Varejo e E-commerce

* Buscador de produto por foto (CLIP)
* Estimativa de estoque por câmera
* Reconhecimento de produto em gôndola

### Mobilidade e Transporte

* Detecção de veículos e pedestres em vídeo
* Contagem de tráfego por câmera
* Leitura de placa (OCR + detecção)

### Criativo / Generativo

* Fine-tuning de Stable Diffusion em estilo artístico específico
* Sistema de remoção de fundo (U-Net)
* Geração de dataset sintético com Stable Diffusion

---

## 🔹 BLOCO 7 — CANDIDATURA E ENTREVISTAS

### Onde Aplicar

**Vagas diretas:**
* LinkedIn (filtrar por "Computer Vision", "PyTorch", "Vision")
* Glassdoor, Indeed
* Site das empresas diretamente

**Comunidades:**
* Discord de ML/IA brasileiro
* Grupos de Visão Computacional no LinkedIn
* HuggingFace Discord

### Preparação Técnica para Entrevistas

**Perguntas comuns:**

1. "Explique backpropagation como se eu tivesse 10 anos"
2. "Quando você usaria transfer learning vs treinar do zero?"
3. "Como você diagnostica overfitting e o que faz?"
4. "Explique a diferença entre CNN e ViT"
5. "Como você faria deploy de um modelo em produção?"
6. "O que é mAP e como você a calcula?"
7. "Você já trabalhou com dados desbalanceados? Como tratou?"

**Para cada resposta:** Conecte à implementação concreta que você fez, não só teoria.

### Take-Home Projects

Muitas empresas enviam projeto para fazer em casa. Estratégia:

1. Entregar em 2-3 dias (sinaliza comprometimento)
2. README profissional (use o template do Bloco 3)
3. Análise de erros incluída (mostra maturidade técnica)
4. Código limpo e documentado
5. Limitações conhecidas honestamente documentadas

### Salário e Negociação

* Pesquisar faixas no Glassdoor por cargo e cidade
* Mencionar seu portfólio e resultados mensuráveis na negociação
* Não aceitar primeira oferta sem questionar

---

## 🧪 ENTREGÁVEIS FINAIS

### 3–5 Projetos de Portfólio

* [ ] README profissional (usar template)
* [ ] Demo funcional (Gradio, Streamlit ou API)
* [ ] Métricas documentadas
* [ ] Código limpo no GitHub
* [ ] Modelo no HuggingFace Hub (quando possível)

### Presença Online

* [ ] GitHub profile README
* [ ] LinkedIn headline e "Sobre" reescritos
* [ ] Pelo menos 4 posts de aprendizado publicados
* [ ] HuggingFace profile com pelo menos 1 modelo

### Candidaturas

* [ ] Mínimo 20 aplicações por semana
* [ ] Personalizar mensagem de candidatura para cada empresa
* [ ] Acompanhar respostas e seguir-up

---

## ⏱ CRONOGRAMA PARALELO

> Esta fase deve rodar **em paralelo** com as outras fases — não espere terminar tudo.

```
Fase 07 (Object Detection) → Começar LinkedIn + 1 projeto de portfólio
Fase 08 (Segmentação)      → 2º projeto de portfólio + perfil GitHub
Fase 09 (MLOps)            → Deploy do projeto → demo ao vivo
Fase 10 (Generativa)       → 3º projeto + posts de aprendizado
Fase 11 (3D)               → 4º projeto + aplicações de vaga
Fase 12 (esta fase)        → Polir tudo, candidaturas ativas
```

---

## ✅ CRITÉRIO REAL DE SAÍDA (DA TRILHA COMPLETA)

Você completou o roadmap quando:

* [ ] Tem 3+ projetos com demo funcional online (não só "código no GitHub")
* [ ] Consegue explicar qualquer projeto em 2 minutos para pessoa não-técnica
* [ ] Consegue explicar os detalhes técnicos em 20 minutos para engenheiro sênior
* [ ] LinkedIn recebe mensagens de recrutadores ativamente
* [ ] Fez ao menos 5 entrevistas técnicas (independente do resultado)
* [ ] Recebeu pelo menos 1 oferta de posição relevante

---

## 📌 VISÃO GERAL COMPLETA DA TRILHA

```
FUNDAMENTOS
├── Fase 00 — Python
├── Fase 01 — Matemática para IA
├── Fase 02 — Machine Learning Clássico

VISÃO CLÁSSICA + DEEP LEARNING
├── Fase 03 — Visão Computacional Clássica
├── Fase 04 — Deep Learning Fundamentals
├── Fase 05 — CNNs e Transfer Learning

MODELO MODERNO + MULTIMODAL
├── Fase 06 — NLP & Transformers (PONTE) ← NOVA

DETECÇÃO E SEGMENTAÇÃO
├── Fase 07 — Object Detection
├── Fase 08 — Segmentação

PRODUÇÃO E FRONTEIRA
├── Fase 09 — MLOps e Produção
├── Fase 10 — IA Generativa 2D        ← SPLIT DA FASE 9 ORIGINAL
├── Fase 11 — Visão 3D e Neural Rendering ← SPLIT DA FASE 9 ORIGINAL

CARREIRA
└── Fase 12 — Portfólio e Carreira    ← NOVA
```

**Duração total estimada:** 3–5 meses com dedicação mínima de 8h por dia (podendo chegar a 12h)  
**Resultado:** Profissional competente para posições de Engenheiro de Visão Computacional ou Engenheiro de ML com especialização em visão


---

