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
