# 🖼️ Fase 05 — Redes Neurais Convolucionais (CNNs) e Transfer Learning

Se a Fase 04 foi onde nós criamos o cérebro, esta Fase 05 é onde o equipamos com **Olhos**.
Você entenderá como as Redes Neurais aprendem Texturas, Bordas, Padrões, Olhos e Rostos Inteiros sem que ninguém lhes explique o que são essas coisas.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_05_CNNs_e_Transfer_Learning/
│
├── Bloco_01_A_Camada_Conv2d/             ← A Base do Scanner Espacial
├── Bloco_02_Feature_Maps/                ← Extraindo e visualizando os filtros (Hooks)
├── Bloco_03_O_Pipeline_Visual/           ← Pooling, Flatten e Redução Espacial
├── Bloco_04_Sua_Primeira_CNN/            ← CNN no MNIST e no Temido CIFAR-10
├── Bloco_05_Data_Augmentation/           ← (Em breve) Mutação de Datasets
├── Bloco_06_Historia_e_ResNets/          ← (Em breve) A Evolução até as Skip Connections
├── Bloco_07_Transfer_Learning_no_Mundo_Real/ ← (Em breve) Como a Indústria Opera
├── Bloco_08_Intro_ViT/                   ← (Em breve) O Fim das CNNs?
└── Projetos_Finais_CNN/                  ← (Em breve)
```

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_anatomia_da_convolucao` | Bloco 01 | 🔴 Crítico |
| 2 | `02_matematica_dos_shapes` | Bloco 01 | 🔴 Crítico |
| 3 | `01_os_olhos_da_rede` | Bloco 02 | 🟠 Importante |
| 4 | `01_pooling_e_flatten` | Bloco 03 | 🔴 Crítico |
| 5 | `01_cnn_no_mnist` | Bloco 04 | 🔴 Crítico |
| 6 | `02_o_desafio_cifar10` | Bloco 04 | 🔴 Crítico |

| 7 | `01_multiplicando_dados` | Bloco 05 | 🔴 Crítico |
| 8 | `01_evolucao_ate_resnet` | Bloco 06 | 🟠 Importante |
| 9 | `01_por_que_nao_comecar_do_zero` | Bloco 07 | 🔴 Crítico |
| 10 | `02_feature_extraction_vs_finetuning` | Bloco 07 | 🔴 Crítico |
| 11 | `01_o_que_sao_patches` | Bloco 08 | 🟢 Opcional (Intro) |
| 12 | `01_CNN_do_Zero` | Projetos Finais | 🔴 Obrigatório |
| 13 | `02_Projeto_Transfer_Learning` | Projetos Finais | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 05)

Antes de ir para a Fase 06 (NLP):
- [ ] Consegue prever o Shape da saída sem precisar rodar um comando PyTorch.
- [ ] Entende por que as Skips Connections da ResNet salvaram o mercado de Deep Learning.
- [ ] Consegue fazer Fine-Tuning substituindo a última "Head" Linear de um modelo VGG/ResNet.
