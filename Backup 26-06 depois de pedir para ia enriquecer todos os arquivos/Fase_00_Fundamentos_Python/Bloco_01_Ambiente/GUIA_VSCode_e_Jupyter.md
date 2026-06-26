# 💻 Guia VSCode e Jupyter Notebook

Em Ciência de Dados, não usamos o bloco de notas. Precisamos de ambientes que permitam rodar código em blocos e inspecionar variáveis dinamicamente.

## 1. Jupyter Notebooks (`.ipynb`)
Notebooks são ideais para **Exploração de Dados** e **Análise Inicial**. Eles misturam código e texto formatado.

### Principais Atalhos:
- `Shift + Enter`: Roda a célula atual e avança para a próxima.
- `Ctrl + Enter`: Roda a célula atual e mantém o cursor nela.
- `A` (fora do modo de edição): Cria uma célula **A**cima (Above).
- `B` (fora do modo de edição): Cria uma célula a**B**aixo (Below).
- `M`: Transforma a célula em Markdown (texto).
- `Y`: Transforma a célula em Código.
- `D, D` (Pressionar D duas vezes): Deleta a célula atual.

## 2. VSCode (Visual Studio Code)
Para projetos em produção (como o seu `Projeto_Final`), você escreverá arquivos Python puros (`.py`). O VSCode é a melhor ferramenta para isso.

### Extensões Obrigatórias:
Vá na aba de extensões (`Ctrl+Shift+X`) e instale:
1. **Python** (da Microsoft)
2. **Pylance** (da Microsoft - Para autocomplete inteligente e Type Hints)
3. **Jupyter** (da Microsoft - Para rodar os notebooks dentro do VSCode)

### O Debugger (A Ferramenta Mais Forte)
Pare de usar `print()` para caçar bugs!
1. Clique ao lado do número da linha de código para criar uma bolinha vermelha (**Breakpoint**).
2. Aperte `F5` para iniciar o código em Modo Debug.
3. O código vai pausar exatamente naquela linha. Você poderá ver o valor de **todas** as variáveis naquele momento exato na tela à esquerda!
4. Use `F10` para avançar linha a linha (`Step Over`).
