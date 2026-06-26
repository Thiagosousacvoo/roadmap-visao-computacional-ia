# FASE 06 — NLP & TRANSFORMERS (PONTE PARA IA MODERNA)

> **Posição na trilha:** NOVA FASE. Ponte obrigatória entre CNNs e IA Generativa/Multimodal.
> **Por que aqui?** ViT, CLIP, Stable Diffusion, GPT-4V — todos dependem de Transformers. Sem esta fase, a Fase 10 (Generativa) não faz sentido.
> **Nível:** Avançado
> **Tempo estimado:** 1–2 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 04 (backprop, PyTorch) e Fase 05 (conceito de ViT)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Deep Learning (Fase 04)

* Backpropagation com regra da cadeia
* `nn.Module`, loops de treino, otimizadores

### CNNs (Fase 05)

* Feature maps, embeddings visuais
* Conceito introdutório de ViT (Bloco 8 da Fase 05)

### Matemática (Fase 01)

* Produto escalar (dot product)
* Multiplicação de matrizes
* Softmax

### Estratégia desta fase

* Foco em **Transformers para Visão** (não em NLP extenso)
* NLP aqui é a ponte — você não vai virar engenheiro de LLM
* O que você **precisa** saber: tokenização, embeddings, atenção, CLIP
* O que você **não precisa** agora: RLHF, fine-tuning de LLMs, RAG

---

## 🔹 BLOCO 1 — REPRESENTAÇÃO DE TEXTO EM NÚMEROS

> Antes de qualquer Transformer, você precisa entender: como texto vira vetor?

### Tokenização

```python
# Texto → lista de tokens (subpalavras)
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer("Um cachorro correndo no parque")
# {'input_ids': [101, 1041, 3232, ..., 102], 'attention_mask': [1,1,...]}
```

**Tipos de tokenização:**
* Word-level: cada palavra = token (vocabulário enorme, palavras desconhecidas)
* Char-level: cada caractere = token (sem OOV, mas sequências longas)
* **Subword (BPE/WordPiece):** palavras comuns inteiras, palavras raras em partes — melhor equilíbrio

### Embeddings

**Word Embedding:** Mapear token (inteiro) → vetor denso (ex: 512 dimensões)

```python
# Camada de embedding
embedding = nn.Embedding(num_embeddings=30000, embedding_dim=512)

# token_id → vetor
vetor = embedding(torch.tensor([42]))  # shape (1, 512)
```

**Por que embedding?**
* `cachorro` e `cão` → vetores próximos
* `cachorro` e `avião` → vetores distantes
* A proximidade no espaço latente captura semântica

**Embeddings de posição (CRÍTICO)**
```python
# Transformer não sabe ordem naturalmente — precisa de position encoding
# Opção 1: Embedding treinável
pos_embedding = nn.Embedding(max_seq_len, d_model)

# Opção 2: Sinusoidal (original do paper "Attention Is All You Need")
# PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
# PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

---

## 🔹 BLOCO 2 — MECANISMO DE ATENÇÃO (CORAÇÃO DO TRANSFORMER)

> Este é o conceito central de toda a IA moderna. Entender atenção = entender GPT, ViT, CLIP, Stable Diffusion.

### Intuição

**Problema:** Ao traduzir "O banco do rio é bonito", como saber que "banco" é margem (não instituição financeira)?

**Solução da atenção:** Ao processar cada palavra, olhar para **todas as outras palavras** e calcular quanta atenção dar a cada uma.

### Scaled Dot-Product Attention

```
Entradas:
  Q (Query)  = "o que estou procurando?"
  K (Key)    = "o que cada token pode oferecer?"
  V (Value)  = "o que cada token realmente contém?"

Operação:
  Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V
```

**Implementação manual:**

```python
import torch
import torch.nn.functional as F

def attention(Q, K, V, mask=None):
    d_k = Q.shape[-1]
    
    # Scores de atenção
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    
    # Opcional: máscara (ex: tokens de padding)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    
    # Softmax → pesos de atenção (somam 1)
    pesos = F.softmax(scores, dim=-1)
    
    # Ponderação dos valores
    return torch.matmul(pesos, V)
```

**Intuição dos pesos:** Se a palavra "rio" recebe peso 0.8 ao processar "banco", a representação final de "banco" vai ser 80% do embedding de "rio" + outras contribuições.

### Multi-Head Attention

```python
# Ao invés de 1 atenção de dimensão d_model,
# usar H atenções paralelas de dimensão d_model/H

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_k = d_model // num_heads
        self.num_heads = num_heads
        
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
    
    def split_heads(self, x):
        B, seq, d = x.shape
        return x.view(B, seq, self.num_heads, self.d_k).transpose(1, 2)
    
    def forward(self, Q, K, V, mask=None):
        Q = self.split_heads(self.W_q(Q))  # (B, H, seq, d_k)
        K = self.split_heads(self.W_k(K))
        V = self.split_heads(self.W_v(V))
        
        attn = attention(Q, K, V, mask)    # (B, H, seq, d_k)
        
        # Concatenar todas as heads
        B, H, seq, d_k = attn.shape
        attn = attn.transpose(1, 2).contiguous().view(B, seq, H*d_k)
        
        return self.W_o(attn)
```

**Por que múltiplas heads?** Cada head aprende a "olhar" para aspectos diferentes da frase:
* Head 1: relações sintáticas (sujeito ↔ verbo)
* Head 2: correferência (pronome ↔ substantivo)
* Head 3: posição relativa

---

## 🔹 BLOCO 3 — ARQUITETURA TRANSFORMER COMPLETA

### Bloco Transformer Encoder

```
Input embeddings + Position encoding
        ↓
┌─────────────────────────────────┐
│  Multi-Head Self-Attention      │
│          + residual + LayerNorm │
├─────────────────────────────────┤
│  Feed-Forward Network           │
│  (Linear → ReLU/GELU → Linear) │
│          + residual + LayerNorm │
└─────────────────────────────────┘
         × N camadas
        ↓
Output: representações contextuais
```

### Self-Attention vs Cross-Attention

**Self-Attention:** Q, K, V vêm da mesma sequência
* Usado em encoder (texto analisa a si mesmo)
* Usado em decoder para análise do output gerado

**Cross-Attention:** Q vem de uma sequência, K e V de outra
* Conecta encoder ao decoder
* **CRÍTICO para visão:** Como texto guia geração de imagem (Q=texto, K,V=imagem)

### Tipos de Transformer

**Encoder-only (BERT):** Representa texto → usado para classificação, NER
**Decoder-only (GPT):** Gera texto → autorregressivo
**Encoder-Decoder (T5, bart):** Sequência → sequência → tradução, sumarização

---

## 🔹 BLOCO 4 — VISION TRANSFORMER (ViT) COMPLETO

> Agora que você entende atenção, ViT faz sentido completo.

### Como a Imagem Vira "Tokens"

```python
class PatchEmbedding(nn.Module):
    def __init__(self, img_size=224, patch_size=16, in_channels=3, d_model=768):
        super().__init__()
        self.num_patches = (img_size // patch_size) ** 2  # 196 patches
        # Conv2d com stride=patch_size extrai patches eficientemente
        self.proj = nn.Conv2d(in_channels, d_model, kernel_size=patch_size, stride=patch_size)
    
    def forward(self, x):
        x = self.proj(x)                    # (B, d_model, H/p, W/p)
        x = x.flatten(2)                    # (B, d_model, num_patches)
        x = x.transpose(1, 2)              # (B, num_patches, d_model)
        return x

# CLS token: token especial para classificação (como em BERT)
cls_token = nn.Parameter(torch.zeros(1, 1, d_model))
# Position embedding: aprendível
pos_embed = nn.Parameter(torch.randn(1, num_patches + 1, d_model))
```

### Vantagem sobre CNN

* CNN: cada neurônio vê apenas vizinhança local
* ViT: cada patch "vê" todos os outros desde a primeira camada (atenção global)
* Para imagens grandes e alta resolução: ViT tende a ser superior com dados suficientes

### 🚧 Exercício

* Implementar ViT simplificado (2-4 camadas) para CIFAR-10
* Comparar com CNN equivalente em número de parâmetros

---

## 🔹 BLOCO 5 — CLIP (CONECTANDO TEXTO E IMAGEM)

> CLIP é o modelo que faz tudo multimodal funcionar: ViT, Stable Diffusion, DALL-E, GPT-4V.

### Como o CLIP Funciona

```
Imagem → Image Encoder (ViT) → vetor de imagem (512d)
Texto  → Text Encoder (Transformer) → vetor de texto (512d)

Treinamento: Contrastive Learning
  - Pares corretos (imagem, legenda) → maximizar similaridade
  - Pares errados → minimizar similaridade
```

### Por que é Revolucionário

* Zero-shot classification: sem treino extra
```python
from PIL import Image
import clip

model, preprocess = clip.load("ViT-B/32")

image = preprocess(Image.open("foto.jpg")).unsqueeze(0)
text = clip.tokenize(["um gato", "um cachorro", "um pássaro"])

with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    
    # Similaridade cosseno
    logits = (image_features @ text_features.T)
    probs = logits.softmax(dim=-1)

print(f"Gato: {probs[0,0]:.2%}, Cachorro: {probs[0,1]:.2%}")
```

### CLIP como Pré-requisito para Stable Diffusion

No Stable Diffusion:
1. Seu prompt de texto → CLIP Text Encoder → vetor de embedding
2. Esse vetor é injetado via **cross-attention** na U-Net
3. A U-Net usa esse vetor para "guiar" o processo de denoising

**Por isso esta fase vem antes da Fase 10 (Generativa).**

---

## 🔹 BLOCO 6 — USANDO HUGGING FACE (PRÁTICO)

> A biblioteca padrão da indústria para Transformers.

```python
from transformers import pipeline, AutoModel, AutoTokenizer

# Zero-shot com pipeline
classifier = pipeline("zero-shot-classification")
resultado = classifier(
    "Esta câmera tem ótima qualidade de imagem",
    candidate_labels=["eletrônicos", "comida", "esporte"]
)

# Extrair embeddings de texto
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

inputs = tokenizer(["frase 1", "frase 2"], return_tensors="pt", padding=True)
outputs = model(**inputs)
embeddings = outputs.last_hidden_state.mean(dim=1)  # Mean pooling

# Similaridade
from torch.nn.functional import cosine_similarity
sim = cosine_similarity(embeddings[0], embeddings[1], dim=0)
```

---

## 🧪 PROJETO FINAL (OBRIGATÓRIO)

### Classificador Zero-Shot com CLIP + Busca Visual

**Objetivo:** Sistema que recebe texto e encontra imagens correspondentes em um dataset.

**Etapas:**

1. Coletar dataset de imagens (ex: 1000 imagens de 10 categorias)
2. Calcular embeddings CLIP para todas as imagens (offline)
3. Interface: usuário digita texto, sistema retorna as 5 imagens mais similares
4. Comparar com classificador CNN treinado na mesma tarefa
5. Analisar casos onde CLIP vence a CNN e vice-versa

**Bônus:** Implementar attention rollout — visualizar quais patches da imagem o ViT "prestou mais atenção"

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Tokenização (conceito + prática com HuggingFace)
2. Embeddings e espaço semântico
3. Position encoding
4. Scaled Dot-Product Attention (implementar do zero)
5. Multi-Head Attention
6. Bloco Transformer Encoder completo
7. Self-Attention vs Cross-Attention
8. ViT: Patch Embedding
9. ViT: implementar e treinar em CIFAR-10
10. CLIP: conceito e uso
11. Zero-shot classification com CLIP
12. HuggingFace: pipelines e extração de embeddings
13. **Projeto Final: Busca visual com CLIP**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Tentar aprender NLP completo (tradução, geração, RLHF) — não é o objetivo aqui
* Usar HuggingFace sem entender o que há por baixo
* Pular implementação manual da atenção
* Não conectar esta fase com Stable Diffusion (Fase 10) — mantenha o "para que serve" em mente

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 07 se:

* [ ] Implementa Self-Attention do zero no PyTorch
* [ ] Explica como o texto guia a geração de imagens (cross-attention)
* [ ] Usa CLIP para classificação zero-shot sem tutorial aberto
* [ ] Entende a diferença entre CNN (local) e ViT (global)
* [ ] Extrai embeddings de texto e compara por similaridade semântica
* [ ] Constrói sistema de busca visual baseado em CLIP
