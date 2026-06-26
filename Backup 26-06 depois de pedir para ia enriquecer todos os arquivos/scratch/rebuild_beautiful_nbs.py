import json
import os

dir_path = r"c:\Desenvolvimento\Especialista em Visão Computacional e IA\Fase_00_Fundamentos_Python\Bloco_1_Fundamentos"

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

# NB1: Tipos de Dados
nb1 = [
    ("markdown", "# 🗂️ Tópico 1: Tipos de Dados\n\nNeste caderno, vamos explorar as fundações da linguagem Python através de cenários práticos e isolados."),
    ("markdown", "## 1. Inteiros (int) e Operações\n\n**Exercício:** \n1. Crie variáveis e faça operações de soma `+`, subtração `-` e multiplicação `*`.\n2. Faça a divisão normal `/` e divisão inteira `//`.\n3. Verifique o módulo `%` (resto da divisão)."),
    ("code", "soma = 1 + 1\nsub = 2 - 1\nmult = 2 * 2\n\n# Escreva o restante aqui:\n\n"),
    ("markdown", "## 2. Float (Decimais)\n\n**Exercício:**\n1. Crie uma variável para a conta de um restaurante (ex: `150.50`).\n2. Calcule 10% de gorjeta.\n3. Use a função nativa `round()` para imprimir o total com apenas 2 casas decimais."),
    ("code", "conta = 150.50\n# Escreva sua lógica de float e arredondamento aqui:\n\n"),
    ("markdown", "## 3. Strings (Textos)\n\n**Exercício:**\nExplore os métodos encadeados das strings na variável abaixo:\n1. Transforme tudo em minúsculas usando `.lower()`.\n2. Remova os espaços em branco (sujeira) das pontas usando `.strip()`.\n3. Troque `.jPg` por `.png` usando `.replace()`.\n4. Divida a string final em uma lista de elementos separados por vírgula usando `.split(',')`."),
    ("code", "texto_sujo = '   aRQuIvO.jPg   '\n# Escreva sua lógica aqui:\n\n"),
    ("markdown", "## 4. Booleanos e Conversões\n\n**Exercício:**\nVerifique se um pesquisador tem permissão para acessar os dados. Ele precisa ter nível de acesso >= 5 **E** ter feito o treinamento.\n*Atenção:* Os dados abaixo vêm como strings (texto). Converta-os com `int()` e `bool()` antes de fazer a checagem lógica!"),
    ("code", "nivel_input = '6'\ntreinamento_input = 'True'\n\n# Converta e escreva sua checagem com 'and', 'or', 'not':\n\n")
]
create_nb("01_tipos_de_dados.ipynb", nb1)

# NB2: Estruturas de Dados
nb2 = [
    ("markdown", "# 🗃️ Tópico 2: Estruturas de Dados\n\nAqui trabalharemos com Listas, Tuplas, Sets e Dicionários de forma bem granular."),
    ("markdown", "## 1. Listas `[]`\n\n**Exercício:** Siga a ordem exata das modificações abaixo.\n1. Adicione o número `40` no final da lista usando `.append()`.\n2. Insira o número `5` exatamente no índice 0 usando `.insert()`.\n3. Remova o número `20` da lista usando `.remove()`.\n4. Extraia o último item da lista e o salve em uma variável usando `.pop()`, depois imprima esse item removido.\n5. Inverta a ordem da lista usando `.reverse()` e a imprima."),
    ("code", "lista_nums = [10, 20, 30]\n# Escreva sua lógica sequencial aqui:\n\n"),
    ("markdown", "## 2. Tuplas `()`\n\nAs tuplas são imutáveis e muito usadas para retornar coordenadas ou múltiplos valores!\n**Exercício:** \n1. Faça o *unpacking* (desempacotamento) das cores abaixo em três variáveis distintas: `R`, `G` e `B` e as imprima.\n2. Tente alterar o valor do `R` diretamente dentro da tupla (`cor_rgb[0] = 200`) para ver o `TypeError` estourar (após ver o erro, comente a linha para não travar o notebook)."),
    ("code", "cor_rgb = (255, 128, 0)\n# Escreva seu desempacotamento aqui:\n\n"),
    ("markdown", "## 3. Sets `{}`\n\nSets removem duplicatas e são ótimos para matemática de conjuntos.\n**Exercício:**\n1. Converta as duas listas abaixo para Sets (isso já removerá os usuários repetidos!).\n2. Descubra a **União** (usuários que acessaram em qualquer um dos turnos).\n3. Descubra a **Interseção** (quais usuários acessaram nos dois turnos simultaneamente)."),
    ("code", "acessos_manha = [1, 2, 2, 3, 4, 5, 1]\nacessos_tarde = [4, 5, 6, 7, 7, 8]\n# Escreva suas operações com sets aqui:\n\n"),
    ("markdown", "## 4. Dicionários `{}`\n\n**Exercício:**\n1. Imprima o nome do modelo acessando a chave `['nome']`.\n2. Adicione uma nova propriedade ao dicionário: a chave `loss` com o valor `0.05`.\n3. Use o método seguro `.get('accuracy', 'N/A')` para tentar pegar uma chave que não existe sem dar erro no programa."),
    ("code", "dados_modelo = {'nome': 'YOLO', 'epochs': 100}\n# Escreva sua manipulação de dicionário aqui:\n\n")
]
create_nb("02_estruturas_de_dados.ipynb", nb2)

# NB3: Condicoes, Loops e Comprehension
nb3 = [
    ("markdown", "# 🔀 Tópicos 3, 4 e 5: Condições, Loops e List Comprehension\n\nControle o fluxo do seu algoritmo."),
    ("markdown", "## 1. Condições (`if`, `elif`, `else`)\n\n**Exercício:** Você está programando o classificador de confiança de uma IA.\n- Se o valor for `>= 0.9`: Imprima 'Detecção Exata'.\n- Se o valor for `>= 0.5`: Imprima 'Detecção Parcial'.\n- Para valores menores que isso: Imprima 'Descartado'."),
    ("code", "predicao = 0.85\n# Escreva seu fluxo de condições aqui:\n\n"),
    ("markdown", "## 2. Loops (`for`, `while`, `break`, `continue`)\n\n**Exercício:** Itere sobre a lista de arquivos abaixo.\n1. Imprima o nome do arquivo APENAS se ele for uma imagem que termina em `.jpg`.\n2. Caso encontre a string `arquivo.corrompido`, interrompa o processamento inteiro imediatamente usando `break`."),
    ("code", "imagens = ['foto1.png', 'foto2.jpg', 'foto3.jpg', 'arquivo.corrompido', 'foto4.jpg']\n# Escreva seu loop aqui:\n\n"),
    ("markdown", "## 3. List Comprehension\n\nEssa é a marca de um programador Python de verdade!\n**Exercício:**\nDada a lista bruta de pixels (que vão de 0 a 255), crie uma **NOVA lista** contendo apenas os pixels que são `> 100`.\nPara esses pixels selecionados que passaram na condição, você já deve dividi-os por 2 na mesma linha.\n\n**Faça tudo isso em uma única linha!**"),
    ("code", "pixels = [10, 50, 120, 200, 45, 180, 255, 90]\n# Escreva seu list comprehension ninja aqui:\n\npixels_filtrados = []\nprint(pixels_filtrados)\n")
]
create_nb("03_condicoes_e_loops.ipynb", nb3)

# NB4: Funcoes e Excecoes
nb4 = [
    ("markdown", "# 🛠️ Tópicos 6, 7 e 8: Funções, Escopo e Exceções\n\nOrganize seu código e lide com quebras."),
    ("markdown", "## 1. Funções e Escopo (Global)\n\n**Exercício:**\n1. O valor de `learning_rate` está no escopo global (fora da função).\n2. Crie uma função chamada `aumentar_lr(fator)` que multiplica essa variável global pelo 'fator' e a atualiza usando a palavra-chave `global`.\n3. Imprima a variável global antes e depois de chamar a função para provar que mudou."),
    ("code", "learning_rate = 0.001\n# Defina e teste sua função aqui:\n\n"),
    ("markdown", "## 2. Lidando com Exceções (`try`, `except`)\n\n**Exercício:**\nVocê criou uma fórmula de precisão, mas ela pode gerar erros dependendo dos dados injetados.\n1. Faça um bloco `try/except` que tenta realizar a divisão abaixo.\n2. Capture o erro específico `ZeroDivisionError` caso os `acertos` sejam 0.\n3. Capture o erro `TypeError` caso você tente dividir um número por uma String.\n4. Adicione o bloco `finally` para imprimir que a validação terminou."),
    ("code", "total_previsto = 100\nacertos = 0 # Mude para 'abc' depois para testar o TypeError\n\n# Escreva seu Try/Except super resiliente aqui:\n\n")
]
create_nb("04_funcoes_e_excecoes.ipynb", nb4)

# NB5: Manipulacao de Arquivos
nb5 = [
    ("markdown", "# 📁 Tópico 9: Manipulação de Arquivos\n\nEscrevendo e Lendo de logs e datasets."),
    ("markdown", "## 1. Escrita (`w` e `a`)\n\n**Exercício:**\n1. Use a função `open()` em modo de escrita completa (`w`) para criar um arquivo chamado `meu_log.txt` e escrever a frase 'INICIO DO TREINO\\n'.\n2. Feche o arquivo.\n3. Abra ele de novo em modo de adição (`a` de append) e acrescente a frase 'Epoch 1 concluída\\n' (sem apagar a primeira!)."),
    ("code", "import os\n# Escreva sua rotina de criação e escrita aqui:\n\n"),
    ("markdown", "## 2. Leitura e CSV Root\n\n**Exercício:**\n1. Abra o `meu_log.txt` e use `.readlines()` para puxar tudo para uma lista.\n2. Na string de CSV solta abaixo, limpe o final com `.strip()` e divida as colunas usando `.split(',')`.\n3. Imprima a lista gerada pelo split."),
    ("code", "linha_do_arquivo = '1,gato,0.88\\n'\n# Extraia os componentes isolados da linha CSV aqui:\n\n")
]
create_nb("05_arquivos.ipynb", nb5)

# NB Mini Projeto
nb_mini = [
    ("markdown", "# 🏆 MINI PROJETO FINAL DO BLOCO 1\n\nNeste desafio, você testará todos os fundamentos (arquivos, loops, dicionários/listas, funções e condições) sem nenhuma biblioteca de dados pronta!"),
    ("markdown", "## 📋 O Problema\nVocê possui o arquivo `dados_funcionarios.csv`.\n1. Leia o arquivo linha por linha usando apenas a função nativa `open()`.\n2. Ao ler cada linha (usando loop `for`), limpe e quebre-a usando o método `.split(',')`.\n3. Aplique a condição: **Você deve selecionar apenas as pessoas com 'salario' maior ou igual a 3000**.\n4. Escreva as pessoas que passaram no filtro em um novo arquivo texto chamado `funcionarios_filtrados.csv` (mantendo o mesmo formato original com vírgulas)."),
    ("markdown", "> 💡 **Dica 1:** O salário lido do arquivo de texto será uma `string`. Você vai precisar convertê-lo com `int()` ou `float()` antes de tentar fazer a comparação `salario >= 3000`!\n>\n> 💡 **Dica 2:** Cuidado com a primeira linha do arquivo original (o cabeçalho `id,nome,idade,cargo,salario`). O cabeçalho não tem um salário numérico, então se você tentar dar `int('salario')` seu código vai quebrar. Uma lógica (como ignorar a primeira linha ou pular exceções) é necessária!"),
    ("code", "def rodar_pipeline(caminho_leitura, caminho_escrita):\n    # Escreva sua lógica completa aqui!\n    pass\n\n# Chamada da função para iniciar:\nrodar_pipeline('dados_funcionarios.csv', 'funcionarios_filtrados.csv')\nprint('Processamento concluído com sucesso!')\n")
]
create_nb("mini_projeto.ipynb", nb_mini)

print("Estrutura linda recriada com sucesso!")
