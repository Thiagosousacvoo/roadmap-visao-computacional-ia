# FASE 12 — PORTFÓLIO E CARREIRA

> **Posição na trilha:** Fase final. Transforma o que você construiu em posicionamento profissional.
> **Nível:** Profissional (estratégia de carreira)
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Quando começar:** Assim que tiver o projeto da Fase 07 (Object Detection) funcionando — não espere acabar tudo

---

## ⚠️ POR QUE ESTA FASE EXISTE

O erro mais comum de quem termina um roadmap técnico extenso:

> "Aprendi muito, mas não consigo me posicionar, não tenho portfólio apresentável e não sei como entrar no mercado."

Esta fase resolve isso sistematicamente. **Não é opcional.**

---

## 🔹 BLOCO 1 — O QUE CONTA COMO PORTFÓLIO

### O que NÃO é portfólio

* "Segui o tutorial do MNIST com 99% accuracy" — Todo mundo tem isso
* "Implementei a U-Net do paper" — Todo mundo que chegou até aqui tem isso
* "Notebook Jupyter com células de código e alguns prints"

### O que É portfólio

* Projeto com **problema real** → você coletou os dados, treinou, avaliou, deployou
* Produto funcional que outra pessoa pode usar (API, app, demo web)
* Solução que resolve algo que você mesmo precisou resolver
* Benchmark/comparação original que gera insight não óbvio

### A Regra de Ouro

**Cada projeto de portfólio deve ter um usuário hipotético que se beneficiaria dele.**

Não: "Treinei YOLO"  
Sim: "Sistema que detecta EPIs em imagens de construção — pode ser usado por apps de segurança do trabalho"

---

## 🔹 BLOCO 2 — SELEÇÃO E MATURAÇÃO DOS PROJETOS

### Quais Projetos Elevar ao Portfólio

**Selecione 3–5 projetos** das fases anteriores que você vai **elevar** — não é criar do zero, é completar e apresentar bem.

**Critérios de seleção:**

| Critério | Peso |
|---|---|
| Problema real (não só exercício acadêmico) | Alto |
| Dataset próprio (você coletou) | Alto |
| Deploy funcional (outra pessoa pode usar) | Alto |
| Resultado mensurável (mAP, accuracy, latência) | Médio |
| Código bem escrito (não notebook bagunçado) | Médio |
| Área que você quer trabalhar | Alto |

### Elevação de Projeto: Checklist

Para cada projeto de portfólio, fazer:

**[ ] Problema claro**
* "Este sistema resolve X para quem tem Y problema"
* Não: "Implementação de YOLO para detecção"
* Sim: "Monitor de segurança em construção: detecta ausência de capacete e emite alerta"

**[ ] Dataset próprio ou com contribuição original**
* Coletar imagens com câmera própria (webcam, celular)
* Ou: usar dataset público MAS adicionar algo original (novas classes, novo split, benchmark)

**[ ] Código limpo e estruturado**
```
projeto/
├── README.md          ← Documentação central (ver Bloco 3)
├── requirements.txt
├── data/
├── src/
│   ├── train.py
│   ├── evaluate.py
│   └── inference.py
├── notebooks/
│   └── exploratory.ipynb
├── models/            ← Pesos do modelo (ou link DVC)
└── demo/              ← Interface ou script de demo
```

**[ ] Métricas documentadas**
* Não: "funciona bem"
* Sim: "mAP@0.5 = 0.87 no conjunto de validação (200 imagens), latência = 23ms em RTX 3060"

**[ ] Demo funcional**
* Streamlit, Gradio, ou API com Swagger (`/docs`)

**[ ] Repositório GitHub com commit history limpo**
* Não commitar modelo .pth (usar DVC ou HuggingFace Hub)
* README com badges de métricas

---

## 🔹 BLOCO 3 — README PERFEITO (TEMPLATE)

```markdown
# [Nome do Projeto] 🔍

> **Uma frase descrevendo o que faz e para quem é útil.**

[Badge CI] [Badge Python] [Badge License]

## Demonstração

![demo.gif](demo.gif)   ← GIF de 10-30s mostrando funcionando

## Problema

[Descrever o problema real. Por que ele importa? Quem tem esse problema?]

## Solução

[Como seu sistema resolve o problema. Qual modelo? Qual abordagem?]

## Métricas

| Métrica | Valor |
|---|---|
| mAP@0.5 | 0.87 |
| Latência (GPU) | 23ms |
| Latência (CPU) | 180ms |
| Dataset | 1.200 imagens / 3 classes |

## Instalação e Uso

\`\`\`bash
git clone https://github.com/seu-usuario/projeto.git
cd projeto
pip install -r requirements.txt

# Demo
python demo.py --source webcam
\`\`\`

## Estrutura do Projeto

[Descrever src/, data/, models/]

## Como Treinei

[Resumo: dataset, tempo de treino, ambiente, decisões técnicas]

## Limitações Conhecidas

[O que o sistema não faz bem. Honestidade = credibilidade]

## Próximos Passos

[O que você faria com mais tempo]
```

---

## 🔹 BLOCO 4 — GITHUB: PRESENÇA PROFISSIONAL

### Profile README

Criar arquivo `github.com/seu-usuario/seu-usuario/README.md`:

```markdown
# Olá, sou [Nome] 👋

Engenheiro de Visão Computacional e IA com foco em sistemas de detecção e segmentação.

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv)

## Projetos em Destaque

| Projeto | Descrição | Métricas |
|---|---|---|
| [Monitor EPI](link) | Detecção de equipamentos de segurança | mAP 0.87 |
| [Análise de Células](link) | Segmentação de imagens médicas | Dice 0.92 |
| [Buscador Visual](link) | CLIP para busca semântica de imagens | — |
```

### Estratégia de Commits

* Commits pequenos e descritivos: "Add Dice loss implementation" não "update"
* Manter repositórios públicos limpos (sem "teste", "temp", "lixo" nos commits)
* Usar releases para versões estáveis: `v1.0.0-alpha`

### HuggingFace Hub

* Publicar modelos treinados no HuggingFace: `model.push_to_hub("seu-usuario/detector-epi")`
* HuggingFace tem inference API gratuita — demo instantâneo

---

## 🔹 BLOCO 5 — LINKEDIN E POSICIONAMENTO

### Headline (não deixar o padrão)

**Ruim:** "Estudante de Ciência da Computação"  
**Melhor:** "Engenheiro de Visão Computacional | PyTorch · YOLO · Segmentação"  
**Melhor ainda:** "Visão Computacional para Segurança Industrial | Detecção de EPIs em Tempo Real"

### Seção "Sobre"

```
Especialista em sistemas de visão computacional com foco em detecção e 
segmentação de objetos aplicados a [área que você quer].

Construí sistemas que [resultado concreto]:
→ Detector de EPIs com mAP 0.87, rodando a 30fps em câmeras IP
→ Pipeline de segmentação de células com Dice score 0.92
→ API de visão containerizada em Docker, servindo 500 req/min

Stack: Python · PyTorch · OpenCV · YOLO · FastAPI · Docker · CUDA
```

### Posts de Aprendizado

Durante o roadmap, publicar **1 post por semana** no LinkedIn sobre o que aprendeu:

* "Entendi hoje por que skip connections da U-Net funcionam — aqui a intuição em 5 pontos"
* "Testei 3 loss functions diferentes para segmentação de células — qual ganhou?"
* "Meu modelo de detecção de capacetes chegou em mAP 0.87 — aqui o que mais ajudou"

**Por que isso funciona:** Recrutadores buscam pessoas que **ensinam**, não só estudam. Post com imagem > post só com texto.

---

## 🔹 BLOCO 6 — PROJETOS DE PORTFÓLIO RECOMENDADOS

Escolha **1 por setor** de interesse:

### Segurança e Industria

* Detector de EPIs (capacete, colete, óculos) em câmeras IP
* Inspeção de qualidade de produto (defeitos na linha de produção)
* Detector de risco em canteiro (pessoa em área proibida)

### Saúde e Medicina

* Segmentação de células em microscópio
* Detecção de objetos em raio-X
* Análise de lesões dermatológicas

### Varejo e E-commerce

* Buscador de produto por foto (CLIP)
* Estimativa de estoque por câmera
* Reconhecimento de produto em gôndola

### Mobilidade e Transporte

* Detecção de veículos e pedestres em vídeo
* Contagem de tráfego por câmera
* Leitura de placa (OCR + detecção)

### Criativo / Generativo

* Fine-tuning de Stable Diffusion em estilo artístico específico
* Sistema de remoção de fundo (U-Net)
* Geração de dataset sintético com Stable Diffusion

---

## 🔹 BLOCO 7 — CANDIDATURA E ENTREVISTAS

### Onde Aplicar

**Vagas diretas:**
* LinkedIn (filtrar por "Computer Vision", "PyTorch", "Vision")
* Glassdoor, Indeed
* Site das empresas diretamente

**Comunidades:**
* Discord de ML/IA brasileiro
* Grupos de Visão Computacional no LinkedIn
* HuggingFace Discord

### Preparação Técnica para Entrevistas

**Perguntas comuns:**

1. "Explique backpropagation como se eu tivesse 10 anos"
2. "Quando você usaria transfer learning vs treinar do zero?"
3. "Como você diagnostica overfitting e o que faz?"
4. "Explique a diferença entre CNN e ViT"
5. "Como você faria deploy de um modelo em produção?"
6. "O que é mAP e como você a calcula?"
7. "Você já trabalhou com dados desbalanceados? Como tratou?"

**Para cada resposta:** Conecte à implementação concreta que você fez, não só teoria.

### Take-Home Projects

Muitas empresas enviam projeto para fazer em casa. Estratégia:

1. Entregar em 2-3 dias (sinaliza comprometimento)
2. README profissional (use o template do Bloco 3)
3. Análise de erros incluída (mostra maturidade técnica)
4. Código limpo e documentado
5. Limitações conhecidas honestamente documentadas

### Salário e Negociação

* Pesquisar faixas no Glassdoor por cargo e cidade
* Mencionar seu portfólio e resultados mensuráveis na negociação
* Não aceitar primeira oferta sem questionar

---

## 🧪 ENTREGÁVEIS FINAIS

### 3–5 Projetos de Portfólio

* [ ] README profissional (usar template)
* [ ] Demo funcional (Gradio, Streamlit ou API)
* [ ] Métricas documentadas
* [ ] Código limpo no GitHub
* [ ] Modelo no HuggingFace Hub (quando possível)

### Presença Online

* [ ] GitHub profile README
* [ ] LinkedIn headline e "Sobre" reescritos
* [ ] Pelo menos 4 posts de aprendizado publicados
* [ ] HuggingFace profile com pelo menos 1 modelo

### Candidaturas

* [ ] Mínimo 20 aplicações por semana
* [ ] Personalizar mensagem de candidatura para cada empresa
* [ ] Acompanhar respostas e seguir-up

---

## ⏱ CRONOGRAMA PARALELO

> Esta fase deve rodar **em paralelo** com as outras fases — não espere terminar tudo.

```
Fase 07 (Object Detection) → Começar LinkedIn + 1 projeto de portfólio
Fase 08 (Segmentação)      → 2º projeto de portfólio + perfil GitHub
Fase 09 (MLOps)            → Deploy do projeto → demo ao vivo
Fase 10 (Generativa)       → 3º projeto + posts de aprendizado
Fase 11 (3D)               → 4º projeto + aplicações de vaga
Fase 12 (esta fase)        → Polir tudo, candidaturas ativas
```

---

## ✅ CRITÉRIO REAL DE SAÍDA (DA TRILHA COMPLETA)

Você completou o roadmap quando:

* [ ] Tem 3+ projetos com demo funcional online (não só "código no GitHub")
* [ ] Consegue explicar qualquer projeto em 2 minutos para pessoa não-técnica
* [ ] Consegue explicar os detalhes técnicos em 20 minutos para engenheiro sênior
* [ ] LinkedIn recebe mensagens de recrutadores ativamente
* [ ] Fez ao menos 5 entrevistas técnicas (independente do resultado)
* [ ] Recebeu pelo menos 1 oferta de posição relevante

---

## 📌 VISÃO GERAL COMPLETA DA TRILHA

```
FUNDAMENTOS
├── Fase 00 — Python
├── Fase 01 — Matemática para IA
├── Fase 02 — Machine Learning Clássico

VISÃO CLÁSSICA + DEEP LEARNING
├── Fase 03 — Visão Computacional Clássica
├── Fase 04 — Deep Learning Fundamentals
├── Fase 05 — CNNs e Transfer Learning

MODELO MODERNO + MULTIMODAL
├── Fase 06 — NLP & Transformers (PONTE) ← NOVA

DETECÇÃO E SEGMENTAÇÃO
├── Fase 07 — Object Detection
├── Fase 08 — Segmentação

PRODUÇÃO E FRONTEIRA
├── Fase 09 — MLOps e Produção
├── Fase 10 — IA Generativa 2D        ← SPLIT DA FASE 9 ORIGINAL
├── Fase 11 — Visão 3D e Neural Rendering ← SPLIT DA FASE 9 ORIGINAL

CARREIRA
└── Fase 12 — Portfólio e Carreira    ← NOVA
```

**Duração total estimada:** 3–5 meses com dedicação mínima de 8h por dia (podendo chegar a 12h)  
**Resultado:** Profissional competente para posições de Engenheiro de Visão Computacional ou Engenheiro de ML com especialização em visão
