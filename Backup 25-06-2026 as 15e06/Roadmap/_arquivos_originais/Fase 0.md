# **⚠️ PRÉ-REQUISITOS NECESSÁRIOS (ANTES DESTA FASE)**

## **🔹 Fundamentos**

### **Lógica de Programação**

* O que é algoritmo  
* Sequência de execução (linha a linha)  
* Estruturas de decisão:  
  * if simples  
  * if/else  
  * if/elif/else  
* Estruturas de repetição:  
  * loop com condição (while)  
  * loop com contador (for conceitual)  
* Variáveis:  
  * criação  
  * atribuição  
  * reatribuição  
* Resolução de problemas:  
  * transformar problema em passos  
  * pseudo-código

👉 Domínio:

* Resolver problemas simples sem copiar código

---

### **Matemática Básica Aplicada**

* Operações:  
  * soma  
  * subtração  
  * multiplicação  
  * divisão  
* Ordem de operações (prioridade)  
* Porcentagem:  
  * calcular %  
  * aplicar desconto  
* Média:  
  * soma / quantidade  
* Noção de vetor:  
  * lista de números  
  * posição (índice)

---

## **🔹 Básico**

### **Ambiente Python**

* Instalar Python  
* Verificar versão (`python --version`)  
* Executar script:  
  * `python arquivo.py`

---

### **Terminal (CLI)**

* Navegação:  
  * `cd`  
  * `ls` / `dir`  
* Criar:  
  * arquivos  
  * pastas  
* Executar comandos

---

### **Arquivos e Pastas**

* Estrutura de diretórios  
* Caminho relativo vs absoluto

---

## **🔹 Intermediário**

### **Importação de módulos**

* import padrão  
* from x import y  
* alias (as)

👉 Domínio:

* Importar qualquer biblioteca sem erro

---

# **🧱 FASE COMPLETA (ULTRA DETALHADA)**

---

# **🔹 BLOCO 1 — FUNDAMENTOS PYTHON**

## **1\. Tipos de Dados**

### **Inteiros (int)**

* operações: \+ \- \* // %  
* comparação

### **Float**

* precisão  
* arredondamento (round)

### **String**

* criação ('', "")  
* concatenação  
* repetição  
* indexação  
* slicing:  
  * \[inicio:fim\]  
  * \[::passo\]  
* métodos:  
  * lower()  
  * upper()  
  * strip()  
  * replace()  
  * split()  
  * join()

### **Boolean**

* True / False  
* operadores:  
  * and  
  * or  
  * not

### **Conversão de tipos**

* int()  
* float()  
* str()

---

## **2\. Estruturas de Dados**

### **Listas**

* criação \[\]  
* acesso por índice  
* slicing  
* métodos:  
  * append()  
  * insert()  
  * remove()  
  * pop()  
  * sort()  
  * reverse()  
* lista dentro de lista

---

### **Tuplas**

* criação ()  
* imutabilidade  
* unpacking

---

### **Sets**

* criação set()  
* remover duplicados  
* operações:  
  * união  
  * interseção

---

### **Dicionários**

* criação {}  
* chave → valor  
* acessar:  
  * dict\["chave"\]  
* métodos:  
  * keys()  
  * values()  
  * items()  
  * get()

---

## **3\. Condições**

* if  
* elif  
* else  
* operadores:  
  * \==  
  * \!=  
  * \<  
  * \=  
  * \<=

---

## **4\. Loops**

### **For**

* iterar lista  
* iterar string

### **While**

* condição de parada

### **Controle**

* break  
* continue

---

## **5\. List Comprehension**

* sintaxe básica  
* com condição  
* aninhado (nível básico)

---

## **6\. Funções**

* def  
* parâmetros:  
  * obrigatórios  
  * opcionais  
* retorno:  
  * return simples  
  * múltiplos valores  
* funções dentro de funções

---

## **7\. Escopo**

* local  
* global  
* leitura vs escrita

---

## **8\. Exceções**

* try  
* except  
* except específico (ValueError, TypeError)  
* else  
* finally

---

## **9\. Arquivos**

### **Leitura**

* open()  
* read()  
* readline()  
* readlines()

### **Escrita**

* write()  
* append

### **CSV (sem pandas)**

* separar por vírgula  
* split()

---

## **🎯 Mini Projeto BLOCO 1**

* Ler CSV manualmente  
* Filtrar linhas com condição  
* Salvar novo CSV

---

# **🔹 BLOCO 2 — PYTHON INTERMEDIÁRIO**

## **1\. Funções Avançadas**

### **\*args**

* múltiplos argumentos posicionais

### **\*\*kwargs**

* múltiplos argumentos nomeados

---

## **2\. Funções como objetos**

* passar função como argumento  
* retornar função

---

## **3\. Lambda**

* sintaxe  
* uso em:  
  * sort  
  * map

---

## **4\. Iteradores**

* conceito de iterável  
* iter()  
* next()

---

## **5\. Geradores**

* yield  
* diferença de return

---

## **6\. enumerate**

* índice \+ valor

---

## **7\. zip**

* combinar listas

---

## **8\. map**

* aplicar função

---

## **9\. filter**

* filtrar com função

---

## **10\. Decorators**

* função que recebe função  
* wrapper  
* conceito de @

---

## **11\. Type Hints**

* tipos em parâmetros  
* tipos de retorno  
* List\[int\], Dict\[str, int\]

---

## **🎯 Mini Projeto BLOCO 2**

* Criar funções reutilizáveis de:  
  * limpeza  
  * transformação  
  * validação

---

# **🔹 BLOCO 3 — POO**

## **1\. Classes**

* class  
* **init**  
* self

---

## **2\. Atributos**

* atributo de instância  
* atributo de classe

---

## **3\. Métodos**

* métodos comuns  
* métodos que retornam valores

---

## **4\. Encapsulamento**

* \_protegido  
* \_\_privado (conceito)

---

## **5\. Herança**

* classe pai  
* classe filha

---

## **6\. Composição**

* classe dentro de classe

---

## **7\. Organização de Projeto**

### **Estrutura:**

* arquivos separados  
* import entre arquivos

---

## **🎯 Mini Projeto BLOCO 3**

* Classe Dataset  
* Classe Processor  
* Classe Saver

---

# **🔹 BLOCO 4 — NUMPY (ULTRA DETALHADO)**

## **Arrays**

* array 1D  
* array 2D

---

## **Criação**

* np.array  
* np.zeros  
* np.ones

---

## **Indexação**

* posição  
* slicing

---

## **Operações**

* soma  
* subtração  
* multiplicação

---

## **Broadcasting**

* regra de compatibilidade

---

## **Álgebra linear**

* np.dot  
* multiplicação de matriz

---

## **Estatística**

* np.mean  
* np.std

---

## **Transformação**

* reshape  
* transpose

---

## **🎯 Domínio**

* NÃO usar for quando puder usar NumPy

---

# **🔹 BLOCO 4.2 — PANDAS**

## **DataFrame**

* criação  
* colunas

---

## **Leitura**

* read\_csv

---

## **Filtragem**

* condições  
* múltiplas condições

---

## **Limpeza**

* dropna  
* fillna

---

## **Agrupamento**

* groupby

---

## **🎯 Domínio**

* Limpar dataset real sozinho

---

# **🔹 BLOCO 4.3 — MATPLOTLIB**

## **Gráficos**

* plot  
* scatter  
* bar

---

## **Imagem**

* imshow

---

## **Customização**

* título  
* labels

---

# **🔹 BLOCO 5 — AMBIENTE**

## **venv**

* criar  
* ativar

---

## **pip**

* install  
* freeze

---

## **requirements.txt**

* gerar  
* instalar

---

## **Jupyter**

* criar notebook  
* rodar células

---

## **VSCode**

* extensões Python  
* debug

---

## **Git**

* init  
* add  
* commit  
* push

---

# **🔹 BLOCO 6 — PERFORMANCE**

## **Complexidade**

* O(n)  
* O(n²)

---

## **Código limpo**

* nomes claros  
* funções pequenas

---

## **Docstring**

* descrição  
* parâmetros  
* retorno

---

## **Logging**

* logging.info  
* logging.error

---

# **🎯 PROJETO FINAL (DETALHADO)**

## **Pipeline completo:**

### **Entrada:**

* CSV

### **Etapas:**

1. Leitura (Pandas)  
2. Limpeza:  
   * remover nulos  
   * corrigir dados  
3. Transformação:  
   * criar novas colunas  
4. Análise:  
   * média  
   * contagem  
5. Visualização:  
   * gráfico  
6. Saída:  
   * salvar CSV novo

---

## **Estrutura:**

project/

├── data/

├── dataset.py

├── processor.py

├── analysis.py

├── utils.py

├── main.py

---

**✅ CRITÉRIO REAL DE SAÍDA**

Você só passou se:

* Não precisa procurar sintaxe básica  
* Consegue estruturar projeto sozinho  
* Resolve erro lendo mensagem  
* Usa NumPy ao invés de loop  
* Código organizado em arquivos

---

