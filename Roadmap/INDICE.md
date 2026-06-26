# 📚 ROADMAP UNIFICADO: ESPECIALISTA EM VISÃO COMPUTACIONAL E IA
> **VERSÃO 2.0 — REVISADA POR ENGENHEIRO SÊNIOR DE VISÃO COMPUTACIONAL**
> Este documento consolida o roadmap original (13 fases) **com todo o conteúdo original preservado integralmente**, mais as correções e adições identificadas em revisão técnica sênior, inseridas diretamente nos pontos corretos da sequência.
>
> Blocos marcados com 🆕 **NOVO** foram adicionados nesta revisão.
> Blocos marcados com 🛠️ **CORRIGIDO** tiveram algo ajustado em relação ao original (erro técnico, termo desatualizado, ou nota de validação temporal).
> Tudo o que não tem marcação é o conteúdo original, inalterado.

---

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
| [06](./Fase%2006%20—%20NLP%20e%20Transformers.md) | NLP & Transformers ⭐ | Avançado | 1–2 sem |
| [07](./Fase%2007%20—%20Object%20Detection.md) | Object Detection | Avançado | 1–2 sem |
| [08](./Fase%2008%20—%20Segmentacao.md) | Segmentação (+ 🆕 Foundation Models) | Avançado | 2–3 sem |
| [09](./Fase%2009%20—%20MLOps%20e%20Producao.md) | MLOps e Produção (+ 🆕 Edge/Robustez/CI) | Profissional | 2–3 sem |
| [10](./Fase%2010%20—%20IA%20Generativa%202D.md) | IA Generativa 2D (+ 🆕 VLMs/SSL) | Estado da Arte | 2–3 sem |
| [11](./Fase%2011%20—%20Visao%203D%20e%20Neural%20Rendering.md) | Visão 3D e Neural Rendering | Estado da Arte | 2–3 sem |
| [12](./Fase%2012%20—%20Portfolio%20e%20Carreira.md) | Portfólio e Carreira | Profissional | Paralelo |

> ⏱ **Nota desta revisão:** o tempo total estimado sobe de "3–5 meses" para **"4–6 meses"** com as adições de 🆕 SAM (Fase 08), edge/quantização/CI (Fase 09) e VLMs/SSL (Fase 10). É esforço real de mercado — não é gordura, é a diferença entre "fiz o tutorial" e "construo o que uma empresa contrataria".

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
└── Fase 08 — Segmentação: U-Net, Mask R-CNN, IoU, pós-processamento, 🆕 SAM/SAM2

PRODUÇÃO (Fase 09)
└── Fase 09 — MLOps: FastAPI, Docker, monitoramento, active learning, 🆕 quantização/edge/CI/robustez

FRONTEIRA (Fases 10-11) ⭐ SPLIT
├── Fase 10 — Generativa 2D: VAE, GAN, Diffusion, LoRA fine-tuning, 🆕 SSL, 🆕 VLMs
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

## ⭐ O QUE FOI MUDADO NA VERSÃO 2.0 (ESTA REVISÃO)

### Resumo da revisão sênior

Esta versão foi revisada por um engenheiro sênior de Visão Computacional com foco em 4 eixos: correção técnica, profundidade vs. fricção desnecessária, lacunas de currículo (o que aparece no dia a dia de trabalho e não estava aqui) e sequenciamento de dependências.

**Veredito geral:** o roadmap original já estava muito acima da média de planos de estudo autodidatas — a filosofia de "implementar manual antes da lib", os critérios de saída explícitos, e a separação Generativo 2D vs. 3D são decisões de design corretas que foram mantidas integralmente. As mudanças abaixo são para levar o roadmap de "muito bom" a "nível do que se cobra de quem contrata".

### 🆕 Lacunas adicionadas (conteúdo novo)

| Onde | O que foi adicionado | Por quê |
|---|---|---|
| Fase 02, Bloco 1 | Nota cruzando entropia/Bayes (Fase 01) com Naive Bayes e calibração de probabilidade | Conexão que existia implicitamente mas não estava explicitada |
| Fase 07, Bloco 3 | RT-DETR comparado lado a lado com YOLO | DETR já era citado como "contexto" mas nunca usado na prática — virou exercício real |
| Fase 07/08 | Bloco curto de OCR (pipeline clássico + Transformer) | Citado nos projetos de portfólio (placas) mas nunca ensinado tecnicamente |
| **Fase 08, Bloco 9** | **SAM / SAM2 (Segment Anything) — bloco completo novo** | Paradigma dominante de segmentação desde 2023+: promptable, zero-shot, sem treinar classe específica |
| Fase 09, Bloco 8 expandido | Quantização real (PTQ vs QAT), pruning, benchmark de latência em hardware restrito | Existia só "exportar para ONNX/TensorRT" sem entrar no trade-off real |
| **Fase 09, Bloco 9** | **Robustez e avaliação fora de distribuição (domain shift)** — bloco novo | Nenhuma fase testava o modelo fora da distribuição de treino — é o que mais quebra sistema em produção |
| **Fase 09, Bloco 10** | **Testes automatizados e CI básico para ML** — bloco novo | Ausente completamente; é o que separa "treinei modelo" de "engenheiro de software de ML" |
| Fase 06/10 | Nota e bloco curto sobre Self-Supervised Learning (SimCLR, DINO) | Resposta de engenharia padrão quando não há volume de dados rotulado — nunca mencionado |
| **Fase 10, Bloco 6** | **VLMs modernos (Vision-Language Models) além do CLIP** — bloco novo | CLIP ensinado corretamente, mas geração de texto sobre imagem (captioning, VQA) nunca aparece |

### Fases Novas (já existentes na v1, mantidas)

| Fase | Motivo |
|---|---|
| **Fase 06 — NLP & Transformers** | Ponte obrigatória: ViT, CLIP, Stable Diffusion, cross-attention dependem disso |
| **Fase 10 — IA Generativa 2D** | Split da Fase 9 original (era grande demais para 1 fase) |
| **Fase 11 — Visão 3D** | Split da Fase 9 original (duas carreiras distintas: Generativo vs 3D/SLAM) |
| **Fase 12 — Portfólio** | Formaliza o que era nota de rodapé — sem portfólio, a trilha não tem impacto |

### 🛠️ Pontos corrigidos/atualizados nesta revisão

| Local | Problema | Correção |
|---|---|---|
| Fase 07, Bloco 3 | "RetinaFocal Loss" mistura dois conceitos | Corrigido para **RetinaNet** (modelo) que **introduziu** a Focal Loss (função de perda) — são coisas diferentes |
| Fase 07, Bloco 4 | Citava número de versão fixo do YOLO como "estado da arte" | Adicionada nota: validar a versão estável mais recente no repositório oficial no momento do estudo — números de versão ficam desatualizados rápido |
| Fase 11, Bloco 6 | Gaussian Splatting descrito como "estado da arte atual" sem ressalva temporal | Adicionada nota de validação temporal — neural rendering evolui rápido, checar CVPR/SIGGRAPH recentes |
| Geral (Fases 10 e 11) | Nenhuma fase de fronteira tinha aviso de "isso pode ter mudado" | Adicionado aviso padrão no topo de toda fase de fronteira |

### Problemas Corrigidos (já existentes na v1, mantidos)

| Problema original | Correção |
|---|---|
| Fase 9 era 3–4 especializações de mestrado em 1 fase | Dividida em Fase 10 (2D) e Fase 11 (3D) |
| Stable Diffusion dependia de CLIP nunca ensinado | Fase 06 ensina CLIP antes |
| Fase 8 (MLOps) misturava conceito e execução sem marcar | Blocos marcados como 🔧 execução ou 📖 conceito |
| Fase 7 (Segmentação) tinha Mask R-CNN no mesmo nível da U-Net | Hierarquia ajustada: U-Net primeiro, Mask R-CNN depois |
| Fase 6 (Detection) não referenciava Fase 3 Bloco 4 (vídeo) | Pré-requisito explicitado |
| Sem fase de portfólio/carreira | Fase 12 criada |
| Artefatos de chat nos arquivos ("Perfeito —", "Vou deixar isso...") | Todos removidos |

### Melhorias de Conteúdo (já existentes na v1, mantidas)

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
* 🆕 **Toda fase de fronteira (06, 08-SAM, 10, 11) deve abrir com uma checagem rápida**: "isto ainda é o que se usa hoje?" — pesquise rapidamente antes de aprofundar. Visão computacional muda mais rápido do que qualquer documento estático consegue acompanhar.

---

*Última atualização desta revisão: Junho 2026*


---

