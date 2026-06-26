# 👀 Fase 03 — Visão Computacional Clássica

Bem vindo à Fase Visual! Onde números viram pixels. Nossa jornada começa dissecando Imagens como simples matrizes NumPy e entendendo a matemática por trás dos filtros, antes de mergulharmos no poderoso ecossistema do OpenCV.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_03_Visao_Computacional_Classica/
│
├── Bloco_01_Imagem_como_Matriz/      ← Dimensões, BGR vs RGB e Crop Numérico
├── Bloco_02_Convolucao_Matematica/   ← (Core) Varredura, Kernels e Sobel
├── Bloco_03_OpenCV_Classico/         ← (Em breve) Contornos, Cores HSV, Limiares
├── Bloco_04_Processamento_de_Video/  ← (Em breve) Loop While, Frame Tracking
└── Projetos_Finais/                  ← (Em breve) Os 4 Desafios Visuais
```

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_rgb_grayscale_e_shape` | Bloco 01 | 🔴 Crítico |
| 2 | `02_acesso_slicing_e_bgr` | Bloco 01 | 🔴 Crítico |
| 3 | `03_io_resize_e_normalizacao` | Bloco 01 | 🟠 Importante |
| 4 | `Mini_Projeto_Brilho_Manual` | Bloco 01 | 🟡 Referência |
| 5 | `01_o_que_e_um_kernel` | Bloco 02 | 🔴 Crítico |
| 6 | `02_convolucao_from_scratch` | Bloco 02 | 🔴 Crítico |
| 7 | `03_filtros_classicos` | Bloco 02 | 🔴 Crítico |

| 8 | `01_bordas_canny_e_sobel` | Bloco 03 | 🔴 Crítico |
| 9 | `02_thresholding_e_binarizacao` | Bloco 03 | 🔴 Crítico |
| 10 | `03_contornos_e_bounding_box` | Bloco 03 | 🔴 Crítico |
| 11 | `04_histogramas_e_cores_hsv` | Bloco 03 | 🔴 Crítico |
| 12 | `05_transformacoes_geometricas` | Bloco 03 | 🟠 Importante |
| 13 | `01_leitura_e_frames` | Bloco 04 | 🔴 Crítico |
| 14 | `02_frame_differencing` | Bloco 04 | 🔴 Crítico |
| 15 | `01_Detector_de_Bordas` | Projetos Finais | 🔴 Obrigatório |
| 16 | `02_Detector_HSV_Interativo` | Projetos Finais | 🔴 Obrigatório |
| 17 | `03_Rastreador_de_Movimento` | Projetos Finais | 🔴 Obrigatório |
| 18 | `04_Pipeline_Rede_Neural.py` | Projetos Finais | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 03)

Antes de ir para a Fase 04 (Deep Learning):
- [ ] Consegue explicar a diferença de multiplicar vetores via Produto Element-wise e Dot Product no contexto das imagens.
- [ ] Entende que OpenCV lê imagens em BGR e o Matplotlib espera RGB.
- [ ] Entende 100% de como um Kernel varre a imagem.
