# 🧠 Fase 04 — Deep Learning Fundamentals

Chegou a hora. Aqui você vai programar os motores matemáticos que sustentam toda a arquitetura de Inteligência Artificial moderna: O Neurônio e o Backpropagation.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_04_Deep_Learning_Fundamentals/
│
├── Bloco_00_Tensores/            ← PyTorch Básico e GPU
├── Bloco_01_Perceptron/          ← Regras de peso, viés e código do zero
├── Bloco_02_Backpropagation/     ← O Caminho de Ida (Forward) e Volta (Backward)
├── Bloco_03_Ativacao_e_Treinamento/ ← (Em breve) Sigmoid, ReLU, Dropout
├── Bloco_04_PyTorch_em_Producao/    ← (Em breve) Dataset, DataLoader e Treino
└── Projeto_Final_MNIST/          ← (Em breve) Código Pytorch Profissional Modular
```

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_introducao_pytorch` | Bloco 00 | 🔴 Crítico |
| 2 | `02_dimensoes_e_gpu` | Bloco 00 | 🔴 Crítico |
| 3 | `Mini_Projeto_Tensores` | Bloco 00 | 🟠 Importante |
| 4 | `01_a_base_do_neuronio` | Bloco 01 | 🔴 Crítico |
| 5 | `02_perceptron_from_scratch` | Bloco 01 | 🔴 Crítico |
| 6 | `01_forward_pass_e_custo` | Bloco 02 | 🔴 Crítico |
| 7 | `02_magia_do_backprop` | Bloco 02 | 🔴 Crítico |
| 8 | `Mini_Projeto_MLP_Numpy` | Bloco 02 | 🔴 Crítico |

| 9 | `01_funcoes_de_ativacao` | Bloco 03 | 🔴 Crítico |
| 10 | `02_hiperparametros_profundos` | Bloco 03 | 🔴 Crítico |
| 11 | `03_dropout_e_batchnorm` | Bloco 03 | 🟠 Importante |
| 12 | `01_datasets_e_dataloaders` | Bloco 04 | 🔴 Crítico |
| 13 | `02_nn_module_e_loops` | Bloco 04 | 🔴 Crítico |
| 14 | `03_monitoramento` | Bloco 04 | 🟠 Importante |
| 15 | `Projeto MNIST End-to-End` | Projeto Final | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 04)

Antes de ir para a Fase 05 (CNNs):
- [ ] Consegue recitar a função mágica do Pytorch (`zero_grad() -> backward() -> step()`).
- [ ] Consegue explicar a diferença de Epochs vs Batch Size.
- [ ] Entende que `loss.backward()` é literalmente apenas o cálculo da regra da cadeia usando Cálculo Diferencial.
