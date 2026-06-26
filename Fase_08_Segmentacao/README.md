# ✂️ Fase 08 — Segmentação de Imagens

Quando "Onde está" não é o suficiente, e você precisa saber "Exatamente a que curva pertence esse pixel?".

Nesta fase aprenderemos as maravilhas da predição pontual e da arquitetura U-Net. É aqui que os famosos algoritmos do Photoshop ou do Zoom de "Remover o Fundo da Câmera" nascem.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_08_Segmentacao/
│
├── Bloco_01_Fundamentos_da_Mascara/     ← A representação de PNGs binários.
├── Bloco_02_Funcoes_de_Perda_e_Metricas/← Dice Loss e Focal Loss (O fim da acurácia).
├── Bloco_03_A_Arquitetura_U_Net/        ← (Em breve) O gargalo da Ampulheta.
├── Bloco_04_Refinamento_e_Avancados/    ← (Em breve) OpenCV Morfológico e Mask R-CNN.
└── Projetos_Finais_Segmentacao/         ← (Em breve)
```

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_tipos_de_segmentacao` | Bloco 01 | 🟠 Importante |
| 2 | `02_representacao_e_dataset` | Bloco 01 | 🔴 Crítico |
| 3 | `01_loss_bce_dice_e_focal` | Bloco 02 | 🔴 Crítico |
| 4 | `02_metricas_iou_e_dice` | Bloco 02 | 🔴 Crítico |

| 5 | `01_anatomia_da_unet` | Bloco 03 | 🔴 Crítico |
| 6 | `02_unet_do_zero_pytorch` | Bloco 03 | 🔴 Crítico |
| 7 | `01_pos_processamento_morfologico` | Bloco 04 | 🟠 Importante |
| 8 | `02_mask_r_cnn` | Bloco 04 | 🟠 Importante |
| 9 | `Projeto_01_Remocao_de_Fundo` | Projetos Finais | 🔴 Obrigatório |
| 10 | `Projeto_02_Treino_UNet_Medica` | Projetos Finais | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 08)

Antes de ir para a Fase 09 (MLOps):
- [ ] Entender a armadilha do Data Augmentation geométrico assíncrono.
- [ ] Implementar a matemática da U-Net com as *Skip Connections* passando pelo funil da rede.
- [ ] Conhecer a diferença brutal entre `BCE Loss` padrão e a punitiva `Dice Loss`.
