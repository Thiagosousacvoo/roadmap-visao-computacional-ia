# 🎯 Fase 07 — Object Detection e Tracking

Esqueça as predições globais. Aqui a Inteligência Artificial vai te dizer o que tem na tela e exatamente em quais coordenadas de pixel o objeto se encontra. O foco total desta fase é preparar você para trabalhar com a biblioteca oficial padrão da indústria: **Ultralytics YOLO**.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_07_Object_Detection/
│
├── Bloco_01_Fundamentos_Bbox/        ← Pascal, YOLO, IoU e a maldita mAP.
├── Bloco_02_Pipeline_de_Dataset/     ← Roboflow, LabelImg e o data.yaml
├── Bloco_03_Familia_YOLO/            ← A guerra dos Detectores: R-CNN x YOLO
├── Bloco_04_Treinamento_Customizado/ ← (Em breve) Como ensinar a rede a ver EPIs industriais
├── Bloco_05_Rastreadores_Tracking/   ← (Em breve) Impedindo que a IA esqueça o id do objeto
├── Bloco_06_Deploy_e_FPS/            ← (Em breve) Hardware Edge e TensorRT
└── Projetos_Finais_Detection/        ← (Em breve)
```

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_formatos_de_caixas` | Bloco 01 | 🔴 Crítico |
| 2 | `02_intersecao_sobre_uniao` | Bloco 01 | 🔴 Crítico |
| 3 | `03_metrica_map` | Bloco 01 | 🔴 Crítico |
| 4 | `01_anotacao_de_dados` | Bloco 02 | 🟠 Importante |
| 5 | `02_formato_yolo` | Bloco 02 | 🔴 Crítico |
| 6 | `01_como_funciona_o_detector` | Bloco 03 | 🟠 Importante |
| 7 | `02_ultralytics_na_pratica` | Bloco 03 | 🔴 Crítico |

| 8 | `01_o_loop_de_treino_yolo` | Bloco 04 | 🔴 Crítico |
| 9 | `01_sort_e_bytetrack` | Bloco 05 | 🔴 Crítico |
| 10 | `01_exportando_onnx_e_tensorrt` | Bloco 06 | 🟠 Importante |
| 11 | `Projeto_Webcam_RealTime` | Projetos Finais | 🔴 Obrigatório |
| 12 | `Projeto_Treino_Customizado` | Projetos Finais | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 07)

Antes de ir para a Fase 08 (Segmentação):
- [ ] O modelo treinado por você bate > 0.70 de mAP no seu próprio Dataset?
- [ ] Sabe a diferença entre Detecção (Detectar frame a frame) e Tracking (Seguir o mesmo objeto via Filtro de Kalman / ByteTrack)?
- [ ] Sabe estruturar pastas e Labels `.txt` compatíveis com YOLOv8?
