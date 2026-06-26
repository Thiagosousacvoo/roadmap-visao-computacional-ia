import json
import os

dir_path = r"c:\Desenvolvimento\Especialista em Visão Computacional e IA\Fase_00_Fundamentos_Python\Bloco_2_Python_Intermediario"

def create_nb(filepath, cells_data):
    cells = []
    for ctype, source in cells_data:
        if ctype == "markdown":
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [s + "\n" for s in source.split("\n")]
            })
        elif ctype == "code":
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [s + "\n" for s in source.split("\n")]
            })
            
    notebook = {
        "cells": cells,
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5
    }
    with open(os.path.join(dir_path, filepath), 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

# NB1: Funções Avançadas e Lambdas
nb1 = [
    ("markdown", "# 🗂️ Tópico 1 a 3: Funções Avançadas, Objetos e Lambdas\n\nAqui começamos a dominar o Python. Entender que tudo é um objeto, até mesmo uma função."),
    ("markdown", "## 1. Funções Avançadas (`*args` e `**kwargs`)\n\n**Exercício:** \n1. Crie uma função `somar_varios(*args)` que receba uma quantidade infinita de números e retorne a soma deles.\n2. Crie uma função `print_config(**kwargs)` que receba parâmetros nomeados (ex: `epochs=100`, `lr=0.01`) e os imprima no formato `Chave: Valor`."),
    ("code", "# Escreva suas funções *args e **kwargs aqui:\n\n"),
    ("markdown", "## 2. Funções como Objetos\n\n**Exercício:**\n1. Crie uma função `multiplicar_por_2(x)`.\n2. Crie uma função `aplicar_operacao(func, valor)` que recebe a função anterior como argumento e a executa com o valor passado.\n3. Teste chamar `aplicar_operacao(multiplicar_por_2, 10)`."),
    ("code", "# Escreva sua lógica de funções como objetos aqui:\n\n"),
    ("markdown", "## 3. Expressões Lambda (Funções Anônimas)\n\n**Exercício:**\n1. Crie uma função lambda que eleva um número ao quadrado e salve-a na variável `quadrado`. Teste-a.\n2. Use uma lambda dentro da função `sort()` ou `sorted()` para ordenar a lista de dicionários abaixo **pela idade** (do mais novo para o mais velho)."),
    ("code", "pessoas = [{'nome': 'Ana', 'idade': 30}, {'nome': 'Beto', 'idade': 25}, {'nome': 'Carlos', 'idade': 40}]\n# Escreva sua lambda e a ordenação aqui:\n\n")
]
create_nb("01_args_kwargs_lambdas.ipynb", nb1)

# NB2: Iteradores e Geradores
nb2 = [
    ("markdown", "# 🗃️ Tópicos 4 e 5: Iteradores e Geradores\n\nEntenda como o Python lida com a memória ao processar grandes volumes de dados (como Datasets de imagens)."),
    ("markdown", "## 1. Iteradores (`iter` e `next`)\n\n**Exercício:**\n1. Pegue a lista `[10, 20, 30]` e transforme-a em um iterador usando a função `iter()`.\n2. Chame a função `next()` três vezes nesse iterador e imprima o resultado a cada chamada.\n3. O que acontece se chamar `next()` uma quarta vez? (Teste e veja a exceção `StopIteration`!)."),
    ("code", "minha_lista = [10, 20, 30]\n# Escreva sua lógica iter e next aqui:\n\n"),
    ("markdown", "## 2. Geradores (`yield`)\n\nGeradores são funções que retornam um valor de cada vez, pausando a execução (`yield` em vez de `return`).\n**Exercício:** \n1. Crie uma função `meu_gerador()` que use `yield` para retornar os números 1, 2 e 3 (um por um).\n2. Itere sobre essa função usando um loop `for` e imprima os valores.\n3. Crie um gerador para ler um arquivo grande fictício linha por linha."),
    ("code", "# Escreva sua função geradora aqui:\n\n")
]
create_nb("02_iteradores_e_geradores.ipynb", nb2)

# NB3: Funções Embutidas
nb3 = [
    ("markdown", "# 🔀 Tópicos 6 a 9: Funções Embutidas (Built-ins)\n\nFunções poderosas para iterar e transformar dados de forma 'Pythônica'."),
    ("markdown", "## 1. `enumerate` (Índice + Valor)\n\n**Exercício:** \nItere sobre a lista abaixo usando `for` e `enumerate()`.\nPara cada item, imprima: `Imagem <índice>: <nome_do_arquivo>`."),
    ("code", "arquivos = ['img_001.jpg', 'img_002.jpg', 'img_003.jpg']\n# Escreva seu enumerate aqui:\n\n"),
    ("markdown", "## 2. `zip` (Combinar listas)\n\n**Exercício:**\nVocê tem uma lista de imagens e uma lista com suas respectivas classes (labels).\nUse um loop `for` junto com `zip()` para iterar sobre ambas ao mesmo tempo e imprimir: `A imagem X é da classe Y`."),
    ("code", "imagens = ['img1', 'img2', 'img3']\nlabels = ['Cachorro', 'Gato', 'Cachorro']\n# Escreva seu zip aqui:\n\n"),
    ("markdown", "## 3. `map` (Aplicar função a todos)\n\n**Exercício:**\nVocê tem uma lista de strings numéricas. \nUse a função `map()` junto com a função `int` para transformar todos os elementos da lista em inteiros puros. Converta o resultado do map para uma lista e imprima."),
    ("code", "strings_num = ['10', '20', '30']\n# Escreva seu map aqui:\n\n"),
    ("markdown", "## 4. `filter` (Filtrar com função)\n\n**Exercício:**\nDada a lista de idades, use a função `filter()` junto com uma função **lambda** para filtrar e manter APENAS as idades `>= 18`. Converta o resultado para lista e imprima."),
    ("code", "idades = [15, 20, 12, 18, 30, 8]\n# Escreva seu filter aqui:\n\n")
]
create_nb("03_funcoes_embutidas.ipynb", nb3)

# NB4: Decorators e Type Hints
nb4 = [
    ("markdown", "# 🛠️ Tópicos 10 e 11: Decorators e Type Hints\n\nAdicione metadados, valide tipos e envolva funções com comportamentos extras."),
    ("markdown", "## 1. Decorators (`@`)\n\nDecorators são 'wrappers' (embrulhos) em torno de funções.\n**Exercício:**\n1. Crie um decorator chamado `medir_tempo` que imprima 'Iniciando função...' antes de rodar a função, execute a função original, e imprima 'Função finalizada!' depois.\n2. Aplique esse decorator usando o `@medir_tempo` em cima de uma função `processar_imagem()`."),
    ("code", "# Escreva seu decorator aqui:\n\n"),
    ("markdown", "## 2. Type Hints (Tipagem Estática Opcional)\n\n**Exercício:**\n1. Importe `List` e `Dict` da biblioteca embutida `typing`.\n2. Crie uma função `calcular_media(notas)` usando Type Hints: especifique que `notas` recebe uma `List[float]` e a função retorna um `float`.\n3. Crie uma variável global usando type hints para definir que ela é um `Dict[str, int]`."),
    ("code", "from typing import List, Dict\n# Escreva suas funções tipadas aqui:\n\n")
]
create_nb("04_decorators_e_typehints.ipynb", nb4)

# NB Mini Projeto
nb_mini = [
    ("markdown", "# 🏆 MINI PROJETO FINAL DO BLOCO 2\n\nAqui não vamos usar o `open()` como no bloco anterior. A ideia é criar um **Módulo de Utilitários** robusto usando conceitos intermediários (Type Hints, kwargs, funções flexíveis e generators)."),
    ("markdown", "## 📋 O Problema\nVocê está criando a base do código da sua empresa de IA. Crie as seguintes funções genéricas:\n\n1. **Função de Limpeza (`limpar_strings`):**\n   - **Input:** `*args` (várias strings passadas soltas).\n   - **Ação:** Deve usar `map` ou List Comprehension para dar um `.strip().lower()` em todas as strings passadas.\n   - **Output:** Retorna a lista das strings limpas.\n   - *Use Type Hints!*\n\n2. **Função Geradora (`ler_em_lotes`):**\n   - **Input:** Uma lista grande (simulando um dataset) e um tamanho de lote (`batch_size`).\n   - **Ação:** Usar `yield` para retornar fatias (`slicing`) dessa lista no tamanho exato do `batch_size`.\n   - **Output:** Um generator que cospe 'lotes' de dados.\n\n3. **Função de Validação Dinâmica (`validar_dados`):**\n   - **Input:** `**kwargs` representando configurações (ex: `min_idade=18`, `status='ativo'`).\n   - **Ação:** Iterar sobre os `.items()` do kwargs e simplesmente imprimir as regras no formato `[VALIDAÇÃO] A chave {k} exige o valor {v}`."),
    ("code", "# 1. Função de Limpeza\n\n\n# 2. Gerador em Lotes\n\n\n# 3. Função de Validação\n\n\n# ----------------------------------------\n# 🚀 TESTE SEU CÓDIGO ABAIXO:\n# ----------------------------------------\n\n# Testando Limpeza:\nprint('Limpos:', limpar_strings(' ARQUIVO.jpg ', '  LABEL_01.PNG'))\n\n# Testando Gerador:\ndataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nfor lote in ler_em_lotes(dataset, batch_size=3):\n    print('Processando lote:', lote)\n\n# Testando Validação:\nvalidar_dados(resolucao='1920x1080', extensao='.png')\n")
]
create_nb("mini_projeto.ipynb", nb_mini)

print("Notebooks do Bloco 2 gerados com sucesso!")
