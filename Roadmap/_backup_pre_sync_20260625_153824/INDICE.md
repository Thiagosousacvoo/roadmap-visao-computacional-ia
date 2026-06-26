# 🗺️ ROADMAP COMPLETO — ESPECIALISTA EM VISÃO COMPUTACIONAL E IA

> Trilha de 3–5 meses para nível profissional com dedicação intensiva
> Dedicação: mínimo 8h por dia (podendo chegar a 12h)

---

## 📋 ÍNDICE DAS FASES

| Fase | Título | Nível | Tempo Est. (8–12h/dia) |
|---|---|---|---|
| [00](./Fase%2000%20—%20Fundamentos%20Python.md) | Fundamentos Python | Iniciante | 1–2 sem |
| [01](./Fase%2001%20—%20Matematica%20para%20IA.md) | Matemática para IA | Básico aplicado | 1–2 sem |
| [02](./Fase%2002%20—%20Machine%20Learning%20Classico.md) | Machine Learning Clássico | Intermediário | 1–2 sem |
| [03](./Fase%2003%20—%20Visao%20Computacional%20Classica.md) | Visão Computacional Clássica | Intermediário | 1 sem |
| [04](./Fase%2004%20—%20Deep%20Learning%20Fundamentals.md) | Deep Learning Fundamentals | Intermediário-Avançado | 1–2 sem |
| [05](./Fase%2005%20—%20CNNs%20e%20Transfer%20Learning.md) | CNNs e Transfer Learning | Avançado | 1–2 sem |
| [06](./Fase%2006%20—%20NLP%20e%20Transformers.md) | NLP & Transformers ⭐ NOVA | Avançado | 1–2 sem |
| [07](./Fase%2007%20—%20Object%20Detection.md) | Object Detection | Avançado | 1–2 sem |
| [08](./Fase%2008%20—%20Segmentacao.md) | Segmentação | Avançado | 1–2 sem |
| [09](./Fase%2009%20—%20MLOps%20e%20Producao.md) | MLOps e Produção | Profissional | 1–2 sem |
| [10](./Fase%2010%20—%20IA%20Generativa%202D.md) | IA Generativa 2D ⭐ NOVA | Estado da Arte | 2–3 sem |
| [11](./Fase%2011%20—%20Visao%203D%20e%20Neural%20Rendering.md) | Visão 3D e Neural Rendering ⭐ NOVA | Estado da Arte | 2–3 sem |
| [12](./Fase%2012%20—%20Portfolio%20e%20Carreira.md) | Portfólio e Carreira ⭐ NOVA | Profissional | Paralelo |

---

## 🗂️ ESTRUTURA DA TRILHA

```
FUNDAMENTOS (Fases 00-02)
├── Fase 00 — Python: tipos, POO, NumPy, Pandas, ambiente
├── Fase 01 — Matemática: álgebra linear, cálculo, probabilidade
└── Fase 02 — ML Clássico: regressão, árvores, métricas, regularização

VISÃO + DEEP LEARNING (Fases 03-05)
├── Fase 03 — Visão Clássica: OpenCV, convolução manual, vídeo
├── Fase 04 — Deep Learning: perceptron, backprop, PyTorch
└── Fase 05 — CNNs: arquiteturas, transfer learning, ViT (introdução)

MODELO MODERNO (Fase 06) ⭐
└── Fase 06 — Transformers: atenção, ViT completo, CLIP, HuggingFace

DETECÇÃO E SEGMENTAÇÃO (Fases 07-08)
├── Fase 07 — Object Detection: YOLO, tracking, mAP, dataset próprio
└── Fase 08 — Segmentação: U-Net, Mask R-CNN, IoU, pós-processamento

PRODUÇÃO (Fase 09)
└── Fase 09 — MLOps: FastAPI, Docker, monitoramento, active learning

FRONTEIRA (Fases 10-11) ⭐ SPLIT
├── Fase 10 — Generativa 2D: VAE, GAN, Diffusion, LoRA fine-tuning
└── Fase 11 — Visão 3D: câmeras, NeRF, Gaussian Splatting, COLMAP

CARREIRA (Fase 12) ⭐
└── Fase 12 — Portfólio: projetos, GitHub, LinkedIn, entrevistas
```

---

## 🔗 DEPENDÊNCIAS ENTRE FASES

```
00 ──→ 01 ──→ 02 ──→ 03 ──→ 04 ──→ 05 ──→ 06 ──→ 07 ──→ 08 ──→ 09
                              ↓                              ↓
                              └──────── 04 ────────→ 10 ────┘
                                        ↓           ↓
                                       05 ──→ 11 ←──┘
                         
Fase 12 corre em paralelo a partir da Fase 07
```

---

## ⭐ O QUE FOI MUDADO NA NOVA VERSÃO

### Fases Novas

| Fase | Motivo |
|---|---|
| **Fase 06 — NLP & Transformers** | Ponte obrigatória: ViT, CLIP, Stable Diffusion, cross-attention dependem disso |
| **Fase 10 — IA Generativa 2D** | Split da Fase 9 original (era grande demais para 1 fase) |
| **Fase 11 — Visão 3D** | Split da Fase 9 original (duas carreiras distintas: Generativo vs 3D/SLAM) |
| **Fase 12 — Portfólio** | Formaliza o que era nota de rodapé — sem portfólio, a trilha não tem impacto |

### Problemas Corrigidos

| Problema original | Correção |
|---|---|
| Fase 9 era 3–4 especializações de mestrado em 1 fase | Dividida em Fase 10 (2D) e Fase 11 (3D) |
| Stable Diffusion dependia de CLIP nunca ensinado | Fase 06 ensina CLIP antes |
| Fase 8 (MLOps) misturava conceito e execução sem marcar | Blocos marcados como 🔧 execução ou 📖 conceito |
| Fase 7 (Segmentação) tinha Mask R-CNN no mesmo nível da U-Net | Hierarquia ajustada: U-Net primeiro, Mask R-CNN depois |
| Fase 6 (Detection) não referenciava Fase 3 Bloco 4 (vídeo) | Pré-requisito explicitado |
| Sem fase de portfólio/carreira | Fase 12 criada |
| Artefatos de chat nos arquivos ("Perfeito —", "Vou deixar isso...") | Todos removidos |

### Melhorias de Conteúdo

| Fase | O que foi adicionado |
|---|---|
| 00 | Logging, decorator, type hints com exemplos reais |
| 01 | Similaridade por cosseno, implementação da descida do gradiente manual |
| 02 | KNN, SVM, Pipeline sklearn, data leakage explicitado |
| 03 | Armadilha BGR/RGB, pipeline de normalização para DL |
| 04 | Tabela ativação por tarefa, curvas de aprendizado, TensorBoard |
| 05 | Tabela de shapes de convolução, bloco residual com código |
| 07 | Código completo IoU, NMS, tabela diagnóstico de modelo |
| 08 | U-Net implementada em PyTorch, tabela quando usar U-Net vs Mask R-CNN |
| 09 | Blocos marcados conceito vs execução, dashboard Streamlit |
| 10 | DCGAN com boas práticas de estabilização, LoRA fine-tuning |
| 11 | Matemática de câmera com código Python completo |

---

## 📌 NOTAS DE USO

* **Critérios de saída são obrigatórios** — não avance sem cumprir
* **Implementação manual antes da biblioteca** é pedagógico, não tortura
* **Fases 10 e 11** são trilhas de especialização independentes — você pode escolher uma delas com mais profundidade dependendo da carreira
* **Fase 12** começa na Fase 07, não no final

---

*Última atualização: Junho 2026*
