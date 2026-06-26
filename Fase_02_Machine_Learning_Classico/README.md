# 🤖 Fase 02 — Machine Learning Clássico

Nesta fase largamos a matemática crua para utilizar ferramentas de alto nível (`scikit-learn`). O objetivo não é apenas chamar uma função `.fit()`, mas entender *quando* usá-la, *por que* ela erra, e *como* resolver overfitting na prática.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_02_Machine_Learning_Classico/
│
├── Bloco_01_Fundamentos/         ← Datasets, X/y, Overfitting e Função de Custo
├── Bloco_02_Algoritmos/          ← R. Linear, Logística, Árvores, KNN, SVM, PCA
├── Bloco_03_Avaliacao/           ← (Em breve) Accuracy, Precision, F1-Score
├── Bloco_04_Ajuste_e_Regularizacao/ ← (Em breve) Grid Search, Pipelines, L1/L2
└── Projeto_Final/                ← (Em breve) Pipeline End-to-End Modular
```

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_conceitos_e_dados` | Bloco 01 | 🔴 Crítico |
| 2 | `02_train_test_split` | Bloco 01 | 🔴 Crítico |
| 3 | `03_funcoes_de_custo` | Bloco 01 | 🔴 Crítico |
| 4 | `04_overfitting_underfitting` | Bloco 01 | 🔴 Crítico |
| 5 | `Mini_Projeto_MSE_Manual` | Bloco 01 | 🟠 Importante |
| 6 | `01_regressao_linear` | Bloco 02 | 🔴 Crítico |
| 7 | `02_regressao_logistica` | Bloco 02 | 🔴 Crítico |
| 8 | `03_arvores_e_florestas` | Bloco 02 | 🔴 Crítico |
| 9 | `04_knn_e_svm` | Bloco 02 | 🟠 Importante |
| 10 | `05_pca_sklearn` | Bloco 02 | 🟠 Importante |
| 11 | `Mini_Projeto_Fronteiras` | Bloco 02 | 🟡 Referência |

| 12 | `01_metricas_classificacao` | Bloco 03 | 🔴 Crítico |
| 13 | `02_metricas_regressao` | Bloco 03 | 🟠 Importante |
| 14 | `Mini_Projeto_Matriz_Confusao` | Bloco 03 | 🔴 Crítico |
| 15 | `01_hiperparametros_e_regularizacao` | Bloco 04 | 🔴 Crítico |
| 16 | `02_cross_val_e_grid_search` | Bloco 04 | 🔴 Crítico |
| 17 | `03_pipelines` | Bloco 04 | 🔴 Crítico |
| 18 | `Projeto_Final (Pipeline)` | Projeto Final | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 02)

Antes de ir para Deep Learning Clássica (Fase 03):
- [ ] Consegue explicar a diferença de SVM vs Árvores de Decisão.
- [ ] Entende que a métrica Accuracy é enganosa em classes desbalanceadas.
- [ ] Detecta Overfitting imediatamente vendo as curvas Treino vs Teste.
- [ ] Consegue usar Pipelines no SKLearn para evitar Data Leakage.
