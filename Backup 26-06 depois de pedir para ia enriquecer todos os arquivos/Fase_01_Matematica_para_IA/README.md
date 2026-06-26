# 🧮 Fase 01 — Matemática para IA

Nesta fase, traduzimos toda a teoria bruta de Álgebra Linear, Cálculo e Estatística em código limpo no NumPy. Você entenderá exatamente como os modelos processam dados no background, dominando a mecânica matemática real da Visão Computacional.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_01_Matematica_para_IA/
│
├── Bloco_01_Vetores/                 ← Criação, Norma, Dot Product, Cosseno
├── Bloco_02_Matrizes/                ← Transformações, Shape, Inversas
├── Bloco_03_Sistemas_Lineares/       ← Regressão Linear Simples
├── Bloco_04_Transformacoes_Lineares/ ← Geometria com Matrizes
├── Bloco_05_Autovalores_e_Autovetores/← Decomposições (Base para PCA)
├── Bloco_06_Calculo_para_IA/         ← Gradientes, Derivadas, Backprop Manual
├── Bloco_07_Probabilidade_e_Estatistica/ ← Distribuições e Bayes
└── Projeto_Final/                    ← Criação de um Modelo PCA do Zero
```

## ⏱️ ORDEM DE EXECUÇÃO

Siga estritamente a sequência dos blocos. A Álgebra Linear ensinada construirá a fundação para que o Cálculo faça sentido. Pule etapas por sua conta e risco.

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_introducao_e_operacoes` | Bloco 01 | 🔴 Crítico |
| 2 | `02_norma_e_dot_product` | Bloco 01 | 🔴 Crítico |
| 3 | `03_similaridade_cosseno` | Bloco 01 | 🔴 Crítico |
| 4 | `Mini_Projeto_Cosseno` | Bloco 01 | 🟠 Importante |
| 5 | `01_dimensao_e_operacoes` | Bloco 02 | 🔴 Crítico |
| 6 | `02_transposta_inversa_det` | Bloco 02 | 🟠 Importante |
| 7 | `Mini_Projeto_Transformacao_2D` | Bloco 02 | 🟡 Referência |

| 8 | `01_conceito_e_np_solve` | Bloco 03 | 🔴 Crítico |
| 9 | `02_sistemas_inconsistentes` | Bloco 03 | 🟠 Importante |
| 10 | `01_rotacao_escala_reflexao` | Bloco 04 | 🟠 Importante |
| 11 | `Mini_Projeto_Animacao_Transformacao` | Bloco 04 | 🟡 Referência |
| 12 | `01_conceito_e_intuicao` | Bloco 05 | 🔴 Crítico |
| 13 | `02_relacao_com_pca` | Bloco 05 | 🔴 Crítico |
| 14 | `Mini_Projeto_Autovetores` | Bloco 05 | 🟠 Importante |
| 15 | `01_derivadas_e_taxa_variacao` | Bloco 06 | 🔴 Crítico |
| 16 | `02_gradiente_e_regra_da_cadeia` | Bloco 06 | 🔴 Crítico |
| 17 | `Mini_Projeto_Descida_do_Gradiente` | Bloco 06 | 🔴 Crítico |
| 18 | `01_estatistica_descritiva` | Bloco 07 | 🔴 Crítico |
| 19 | `02_distribuicoes` | Bloco 07 | 🔴 Crítico |
| 20 | `03_bayes_e_entropia` | Bloco 07 | 🟠 Importante |
| 21 | `Exploracao_PCA` | Projeto Final | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 01)

Antes de ir para Machine Learning (Fase 02), confirme:
- [ ] Consegue explicar a diferença de multiplicar vetores via Produto Element-wise e Dot Product.
- [ ] Prevê de cabeça qual será o Shape (N, M) resultante de uma multiplicação matricial.
- [ ] Sabe o que um Gradiente representa e como ele ajuda um modelo a aprender.
- [ ] Entende que PCA reduz dimensionalidade através da análise da variância e covariância dos dados.
