# 🐍 FASE 00 — FUNDAMENTOS DE PYTHON

> **Nível:** Iniciante → Intermediário  
> **Tempo estimado:** 1–2 semanas (8–12h/dia)  
> **Objetivo:** Dominar Python com foco em ciência de dados e IA

---

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_00_Fundamentos_Python/
│
├── Bloco_01_Fundamentos_Python/       ← Tipos, estruturas, funções, arquivos
│   ├── 01_tipos_de_dados.ipynb
│   ├── 02_estruturas_de_dados.ipynb
│   ├── 03_condicoes_e_loops.ipynb
│   ├── 04_funcoes.ipynb
│   ├── 05_excecoes_e_arquivos.ipynb
│   └── Mini_Projeto_Pipeline_CSV.ipynb
│
├── Bloco_02_Python_Intermediario/     ← Args, lambda, geradores, decorators
│   ├── 01_funcoes_avancadas.ipynb
│   ├── 02_funcoes_ordem_superior.ipynb
│   ├── 03_iteradores_e_geradores.ipynb
│   ├── 04_decorators.ipynb
│   ├── 05_type_hints.ipynb
│   └── Mini_Projeto_Funcoes_Reutilizaveis.ipynb
│
├── Bloco_03_POO/                      ← Classes, herança, composição
│   ├── 01_classes_e_instancias.ipynb
│   ├── 02_metodos_e_encapsulamento.ipynb
│   ├── 03_heranca_e_composicao.ipynb
│   ├── 04_organizacao_de_projeto.ipynb
│   └── Mini_Projeto_Dataset_Processor_Saver.ipynb
│
├── Bloco_04_NumPy/                    ← Arrays, operações, álgebra linear
│   ├── 01_arrays_e_criacao.ipynb
│   ├── 02_indexacao_e_slicing.ipynb
│   ├── 03_operacoes_vetorizadas.ipynb
│   ├── 04_broadcasting.ipynb
│   ├── 05_algebra_linear.ipynb
│   ├── 06_estatistica.ipynb
│   └── 07_transformacao.ipynb
│
├── Bloco_04_2_Pandas/                 ← DataFrame, filtragem, limpeza
│   ├── 01_dataframe_basico.ipynb
│   ├── 02_leitura_e_escrita.ipynb
│   ├── 03_filtragem.ipynb
│   ├── 04_limpeza_de_dados.ipynb
│   └── 05_agrupamento_e_agregacao.ipynb
│
├── Bloco_04_3_Matplotlib/             ← Visualização de dados
│   ├── 01_graficos_basicos.ipynb
│   ├── 02_imshow_e_imagens.ipynb
│   └── 03_customizacao_e_subplots.ipynb
│
├── Bloco_05_Ambiente/                 ← venv, pip, Jupyter, Git
│   ├── GUIA_Ambiente_Virtual.md
│   ├── GUIA_Git_Essencial.md
│   └── GUIA_VSCode_e_Jupyter.md
│
├── Bloco_06_Qualidade_de_Codigo/      ← Complexidade, docstrings, logging
│   ├── 01_complexidade_algoritmica.ipynb
│   ├── 02_codigo_limpo_e_docstrings.ipynb
│   └── 03_logging.ipynb
│
└── Projeto_Final/                     ← Pipeline completo de dados
    ├── README.md
    ├── data/
    │   ├── raw/
    │   └── processed/
    ├── src/
    │   ├── dataset.py
    │   ├── processor.py
    │   ├── analysis.py
    │   └── utils.py
    ├── main.py
    └── Exploracao_e_Desenvolvimento.ipynb
```

---

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_tipos_de_dados` | Bloco 01 | 🔴 Crítico |
| 2 | `02_estruturas_de_dados` | Bloco 01 | 🔴 Crítico |
| 3 | `03_condicoes_e_loops` | Bloco 01 | 🔴 Crítico |
| 4 | `04_funcoes` | Bloco 01 | 🔴 Crítico |
| 5 | `05_excecoes_e_arquivos` | Bloco 01 | 🔴 Crítico |
| 6 | `Mini_Projeto_Pipeline_CSV` | Bloco 01 | 🔴 Obrigatório |
| 7 | `01_funcoes_avancadas` | Bloco 02 | 🟠 Importante |
| 8 | `02_funcoes_ordem_superior` | Bloco 02 | 🟠 Importante |
| 9 | `03_iteradores_e_geradores` | Bloco 02 | 🟠 Importante |
| 10 | `04_decorators` | Bloco 02 | 🟠 Importante |
| 11 | `05_type_hints` | Bloco 02 | 🟠 Importante |
| 12 | `Mini_Projeto_Funcoes_Reutilizaveis` | Bloco 02 | 🟠 Obrigatório |
| 13 | `01_classes_e_instancias` | Bloco 03 | 🔴 Crítico |
| 14 | `02_metodos_e_encapsulamento` | Bloco 03 | 🔴 Crítico |
| 15 | `03_heranca_e_composicao` | Bloco 03 | 🟠 Importante |
| 16 | `04_organizacao_de_projeto` | Bloco 03 | 🟠 Importante |
| 17 | `Mini_Projeto_Dataset_Processor_Saver` | Bloco 03 | 🔴 Obrigatório |
| 18 | `01_arrays_e_criacao` | Bloco 04 | 🔴 Crítico |
| 19 | `02_indexacao_e_slicing` | Bloco 04 | 🔴 Crítico |
| 20 | `03_operacoes_vetorizadas` | Bloco 04 | 🔴 Crítico |
| 21 | `04_broadcasting` | Bloco 04 | 🔴 Crítico |
| 22 | `05_algebra_linear` | Bloco 04 | 🔴 Crítico |
| 23 | `06_estatistica` | Bloco 04 | 🔴 Crítico |
| 24 | `07_transformacao` | Bloco 04 | 🔴 Crítico |
| 25 | `01_dataframe_basico` | Bloco 04.2 | 🔴 Crítico |
| 26 | `02_leitura_e_escrita` | Bloco 04.2 | 🔴 Crítico |
| 27 | `03_filtragem` | Bloco 04.2 | 🔴 Crítico |
| 28 | `04_limpeza_de_dados` | Bloco 04.2 | 🔴 Crítico |
| 29 | `05_agrupamento_e_agregacao` | Bloco 04.2 | 🔴 Crítico |
| 30 | `01_graficos_basicos` | Bloco 04.3 | 🟠 Importante |
| 31 | `02_imshow_e_imagens` | Bloco 04.3 | 🟠 Importante |
| 32 | `03_customizacao_e_subplots` | Bloco 04.3 | 🟠 Importante |
| 33 | `GUIA_Ambiente_Virtual` | Bloco 05 | 🟡 Referência |
| 34 | `GUIA_Git_Essencial` | Bloco 05 | 🟡 Referência |
| 35 | `GUIA_VSCode_e_Jupyter` | Bloco 05 | 🟡 Referência |
| 36 | `01_complexidade_algoritmica` | Bloco 06 | 🟠 Importante |
| 37 | `02_codigo_limpo_e_docstrings` | Bloco 06 | 🟠 Importante |
| 38 | `03_logging` | Bloco 06 | 🟠 Importante |
| 39 | `Exploracao_e_Desenvolvimento` | Projeto Final | 🔴 Obrigatório |

---

## ✅ CRITÉRIOS DE SAÍDA (FASE 00)

Antes de ir para a Fase 01, confirme:

- [ ] Não precisa consultar sintaxe básica de Python
- [ ] Estrutura projeto em múltiplos arquivos sem tutorial
- [ ] Lê traceback de erro e resolve sozinho
- [ ] Usa NumPy ao invés de loops onde possível
- [ ] Implementa POO de forma natural
- [ ] Código com docstrings e logging

---

*🔗 Próxima fase: [Fase 01 — Matemática para IA](../Roadmap/Fase%2001%20—%20Matematica%20para%20IA.md)*
