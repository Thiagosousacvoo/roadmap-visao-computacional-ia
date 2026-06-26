# 🌉 Fase 06 — NLP e Transformers (A Ponte Multimodal)

Esta é a fase teórica mais complexa até o momento.
Por que um especialista em Imagens e Vídeos tem que entender de Processamento de Linguagem (NLP)?
Porque o mundo evoluiu. A Convolução (CNN) isolada já não é suficiente.
A OpenAI com o ChatGPT, CLIP, DALL-E e o Vision Transformer (ViT) provaram que as IAs conversam melhor através de Redes de "Atenção".

Você irá dissecar a Atenção e aprender como amarrar Texto em Imagem.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_06_NLP_e_Transformers/
│
├── Bloco_01_Texto_em_Numeros/            ← O Espaço Geométrico dos Embeddings
├── Bloco_02_O_Coracao_do_Transformer/    ← O Mecanismo Scaled Dot-Product Attention
├── Bloco_03_A_Arquitetura_Completa/      ← Encoders e Decoders
├── Bloco_04_Vision_Transformers_ViT/     ← (Em breve) Fatiando as Imagens (Fim da CNN)
├── Bloco_05_A_Revolucao_Multimodal/      ← (Em breve) CLIP (A Magia de Juntar Imagem e Texto)
├── Bloco_06_Hugging_Face/                ← (Em breve) O Padrão Ouro do Código Moderno
└── Projetos_Finais_Transformers/         ← (Em breve)
```

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_tokenizacao_e_vocabulario` | Bloco 01 | 🔴 Crítico |
| 2 | `02_espaco_latente_embeddings` | Bloco 01 | 🔴 Crítico |
| 3 | `03_positional_encoding` | Bloco 01 | 🟠 Importante |
| 4 | `01_mecanismo_de_atencao_manual` | Bloco 02 | 🔴 Crítico |
| 5 | `02_multi_head_attention` | Bloco 02 | 🔴 Crítico |
| 6 | `01_encoder_e_residual_connections` | Bloco 03 | 🔴 Crítico |

| 7 | `01_imagens_como_palavras` | Bloco 04 | 🔴 Crítico |
| 8 | `01_a_magia_do_clip` | Bloco 05 | 🔴 Crítico |
| 9 | `01_a_biblioteca_definitiva` | Bloco 06 | 🟠 Importante |
| 10 | `Projeto_Busca_Visual_CLIP` | Projetos Finais | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 06)

Antes de ir para a Fase 07 (Object Detection):
- [ ] Entender perfeitamente o formato `Query, Key e Value` do Self-Attention.
- [ ] Conseguir explicar como o CLIP (OpenAI) entende de imagens sendo que ele classifica com Texto.
- [ ] Construir a base conceitual do ViT e saber por que ele vence as CNNs em alta escala.
