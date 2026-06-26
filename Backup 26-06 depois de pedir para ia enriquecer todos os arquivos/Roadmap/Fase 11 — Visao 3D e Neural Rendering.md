# FASE 11 — VISÃO 3D E NEURAL RENDERING

> **Posição na trilha:** Segunda metade da Fase 9 original — trilha de carreira independente (Visão 3D, SLAM, Robótica, XR).
> **Nível:** Estado da Arte (Pesquisa aplicada)
> **Tempo estimado:** 2–3 semanas (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 04 (PyTorch sólido), Fase 05 (CNNs), Fase 08 (segmentação — para U-Net e 🆕 SAM)

> ⚠️ 🆕 **Nota de validação temporal (esta revisão):** neural rendering é uma das áreas que mais evolui rápido em toda a visão computacional. O Bloco 6 (3D Gaussian Splatting) descreve o que era estado da arte em 2023-2024 — antes de investir semanas de estudo, faça uma checagem rápida em CVPR/SIGGRAPH recentes para confirmar se ainda é a abordagem dominante ou se já existe sucessor mais relevante.

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### Matemática (Fase 01 — mas agora 3D)

* **Álgebra Linear Espacial (CRÍTICO):**
  * Matrizes de rotação e translação
  * Homogeneous coordinates (coordenadas homogêneas)
  * Produto de matrizes de transformação

### PyTorch

* Implementar MLP customizado
* Custom loss functions
* Gradiente fluindo por operações não-triviais

### Visão Computacional Clássica (Fase 03)

* Manipulação de imagem
* Coordenadas de pixel

---

## 🔹 BLOCO 1 — MATEMÁTICA DA CÂMERA 3D (BASE ABSOLUTA)

> Sem isso, NeRF e Gaussian Splatting são magia incompreensível. Com isso, são engenharia.

### Por que a câmera importa?

Toda reconstrução 3D parte desta pergunta: "Como um ponto (X, Y, Z) no mundo vira o pixel (u, v) na tela?"

### Coordenadas Homogêneas

```
Ponto 3D no mundo:  P_w = [X, Y, Z, 1]ᵀ   (4D com 1 no final)
Ponto 2D na imagem: p = [u, v, 1]ᵀ        (3D com 1 no final — homogêneo)
```

Por que adicionar 1? Permite representar translação como multiplicação de matriz — elegância matemática.

### Câmera Extrínseca [R | t] — Onde a Câmera Está no Mundo

```
        [R₃ₓ₃ | t₃ₓ₁]
[R|t] = [             ]  ← 3×4
        
R: Matriz de rotação 3×3 (orientação da câmera)
t: Vetor de translação 3×1 (posição da câmera)
```

**Transformar ponto do mundo para câmera:**
```python
# P_camera = R @ P_world + t
P_camera = R @ P_world + t
```

**Interpretação:** Se você mover a câmera 1m para direita, `t` muda. Se você girar a câmera 30° para esquerda, `R` muda.

### Câmera Intrínseca K — A Lente

```
    [fx  0   cx]
K = [0   fy  cy]    ← 3×3
    [0   0    1]

fx, fy: Focal length em pixels (quanto a câmera "amplia")
cx, cy: Centro óptico da imagem (normalmente W/2, H/2)
```

### Projeção Completa (Pinhole Model)

```python
def projetar_ponto_3d(P_world, R, t, K):
    """
    P_world: ponto 3D no mundo (3,)
    R: matriz de rotação (3,3)
    t: translação (3,)
    K: intrínsecos (3,3)
    Retorna: ponto 2D na imagem (u, v)
    """
    # 1. Mundo → Câmera
    P_cam = R @ P_world + t    # (3,)
    
    # 2. Câmera → Imagem (projeção perspectiva)
    P_img_hom = K @ P_cam      # (3,)
    
    # 3. Normalizar coordenadas homogêneas
    u = P_img_hom[0] / P_img_hom[2]
    v = P_img_hom[1] / P_img_hom[2]
    
    return u, v
```

### 🚧 Exercício Fundamental

* Criar cena 3D simples (cubo de pontos)
* Projetar de 4 ângulos diferentes (variando R e t)
* Verificar que projeção corresponde ao que você esperaria visualmente

---

## 🔹 BLOCO 2 — REPRESENTAÇÕES 3D

> Antes de aprender modelos 3D neurais, entender as representações clássicas.

### Point Clouds (Nuvens de Pontos)

```python
import numpy as np
import open3d as o3d

# Array Nx3 (N pontos, cada um com X, Y, Z)
pontos = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], ...])

# Visualizar com Open3D
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pontos)
o3d.visualization.draw_geometries([pcd])
```

**Vantagens:** Simples, diretamente de LiDAR e câmeras de profundidade  
**Desvantagens:** Esparsa, sem superfície explícita

### Voxel Grids

```
3D grid de células (como pixels mas 3D)
Resolução 64³ → 262.144 células
Resolução 256³ → 16.777.216 células   ← memória explode
```

**Problema:** `O(N³)` — inviável em alta resolução

### Meshes (Malhas 3D)

```python
# Vértices + Faces (triângulos)
vertices = [[0,0,0], [1,0,0], [0,1,0], [0,0,1]]  # 4 vértices
faces = [[0,1,2], [0,1,3], [0,2,3], [1,2,3]]      # 4 triângulos

mesh = o3d.geometry.TriangleMesh()
mesh.vertices = o3d.utility.Vector3dVector(vertices)
mesh.triangles = o3d.utility.Vector3iVector(faces)
```

**Padrão da indústria:** jogos, animação, manufatura  
**Problema:** Difícil de reconstruir automaticamente de fotos

### Representações Neurais (Implícitas)

* A cena 3D é codificada nos **pesos de uma rede neural** — não em arquivo .obj
* Consulta: "Qual a cor/densidade deste ponto (x,y,z)?"
* Resposta: rodar o MLP naquelas coordenadas

---

## 🔹 BLOCO 3 — ESTIMATIVA DE PROFUNDIDADE

### Visão Estéreo

```
Câmera Esquerda  |  Câmera Direita
     ────────────────────────
                    d (disparidade)
     
Profundidade Z = f * B / d
onde:
  f = focal length
  B = baseline (distância entre câmeras)
  d = disparidade em pixels (objeto longe → disparidade pequena)
```

**Como os humanos veem em 3D:** Exatamente o mesmo princípio — dois olhos separados horizontalmente.

```python
import cv2

# Computar disparidade com OpenCV
stereo = cv2.StereoBM.create(numDisparities=96, blockSize=15)
disparity = stereo.compute(img_left, img_right)

# Converter disparidade → profundidade
depth = (focal * baseline) / (disparity + 1e-6)
```

### Monocular Depth Estimation (Uma só câmera)

```python
from transformers import pipeline

# MiDaS ou DepthAnything — estado da arte
depth_estimator = pipeline("depth-estimation", model="depth-anything/Depth-Anything-V2-Small")

img = Image.open("foto.jpg")
resultado = depth_estimator(img)
mapa_profundidade = resultado['predicted_depth']  # Valores relativos

# Visualizar
plt.imshow(mapa_profundidade, cmap='plasma')
plt.colorbar(label='Profundidade (relativa)')
```

### Criar Point Cloud a partir de Depth Map

```python
def depth_to_pointcloud(depth_map, K):
    """
    depth_map: (H, W) mapa de profundidade
    K: matrix intrínseca (3,3)
    Retorna: (N, 3) nuvem de pontos
    """
    H, W = depth_map.shape
    fx, fy = K[0,0], K[1,1]
    cx, cy = K[0,2], K[1,2]
    
    u, v = np.meshgrid(np.arange(W), np.arange(H))
    z = depth_map
    x = (u - cx) * z / fx
    y = (v - cy) * z / fy
    
    pontos = np.stack([x, y, z], axis=-1).reshape(-1, 3)
    return pontos[pontos[:, 2] > 0]  # Remover pontos inválidos
```

### 🚧 Exercício

1. Tirar foto de objeto na mesa
2. Rodar DepthAnything
3. Converter mapa de profundidade em point cloud 3D
4. Visualizar no Open3D

---

## 🔹 BLOCO 4 — COLMAP E STRUCTURE FROM MOTION

> COLMAP é o padrão da indústria para extrair geometria 3D de fotos comuns.

### Structure from Motion (SfM): Intuição

**Problema:** Tenho 100 fotos do mesmo objeto. Onde cada câmera estava?  
**Solução:** Encontrar pontos comuns entre fotos → triangular posição 3D → resolver posição das câmeras.

```
Fotos de múltiplos ângulos
    ↓
SIFT / SuperPoint → Features em cada imagem
    ↓
Feature Matching → Quais features são o mesmo ponto 3D?
    ↓
RANSAC + Triangulação → Posição 3D dos pontos
    ↓
Bundle Adjustment → Otimizar cameras + pontos simultaneamente
    ↓
Saída: Matrizes R, t de cada câmera + sparse point cloud
```

### Usar COLMAP na Prática

```bash
# Instalar COLMAP (Windows: colmap.github.io)

# 1. Estrutura de pastas
mkdir meu_objeto
mkdir meu_objeto/images

# 2. Colocar imagens em meu_objeto/images/

# 3. Rodar pipeline automático
colmap automatic_reconstructor \
    --workspace_path meu_objeto/ \
    --image_path meu_objeto/images/

# Saída:
# meu_objeto/sparse/0/cameras.bin   ← Intrínsecos K por câmera
# meu_objeto/sparse/0/images.bin    ← Extrínsecos R,t por imagem
# meu_objeto/sparse/0/points3D.bin  ← Sparse point cloud
```

### Ler Saída do COLMAP em Python

```python
import pycolmap

rec = pycolmap.Reconstruction("meu_objeto/sparse/0")

for img_id, img in rec.images.items():
    R = img.rotation_matrix()   # 3×3
    t = img.tvec                # 3,
    print(f"Câmera {img.name}: posição aproximada {-R.T @ t}")

# Exportar point cloud
points = np.array([p.xyz for p in rec.points3D.values()])
print(f"Pontos 3D: {points.shape}")
```

---

## 🔹 BLOCO 5 — NeRF (NEURAL RADIANCE FIELDS)

> NeRF revolucionou reconstrução 3D em 2020. A cena inteira vive dentro dos pesos de um MLP.

### Como Funciona

```
Entrada do MLP:
  (x, y, z)      ← Ponto 3D no espaço
  (θ, φ)          ← Ângulo de visão (direção do raio)

Saída do MLP:
  (R, G, B)       ← Cor daquele ponto naquele ângulo
  σ               ← Densidade (quão sólido está o ponto)
```

### Volume Rendering (A Magia)

Para gerar um pixel: disparar raio da câmera através da cena, amostrar N pontos ao longo do raio, acumular cores e densidades:

```python
def volume_render(colors, sigmas, deltas):
    """
    colors: (N, 3) — cor de cada ponto amostrado
    sigmas: (N,)   — densidade de cada ponto
    deltas: (N,)   — distância entre pontos consecutivos
    Retorna: cor final do pixel (3,)
    """
    # Transmitância: quanto de luz "passou" até este ponto
    alpha = 1 - torch.exp(-sigmas * deltas)
    
    # Produto cumulativo de transparências anteriores
    transmitancia = torch.cumprod(
        torch.cat([torch.ones((1,)), 1 - alpha[:-1]]), dim=0
    )
    
    # Pesos: contribuição de cada ponto para o pixel
    pesos = alpha * transmitancia  # (N,)
    
    # Cor final: soma ponderada
    cor_pixel = (pesos[:, None] * colors).sum(dim=0)  # (3,)
    
    return cor_pixel
```

### Loss do NeRF

```python
# Simples: comparar cor renderizada com cor real do pixel
loss = F.mse_loss(cor_renderizada, cor_pixel_real)
```

**O modelo aprende:** Ajustar os pesos do MLP para que, ao renderizar de qualquer ângulo, a imagem gerada bata com as fotos reais. Depois de treinado, pode gerar de **qualquer ângulo nunca visto**.

### Implementação Mínima

```python
class NeRFMLP(nn.Module):
    def __init__(self, pos_enc_dim=10, dir_enc_dim=4):
        super().__init__()
        # Positional encoding aumenta dimensionalidade para capturar detalhes finos
        in_dim = 3 + 3*2*pos_enc_dim  # xyz + senos/cossenos
        
        self.net = nn.Sequential(
            nn.Linear(in_dim, 256), nn.ReLU(),
            nn.Linear(256, 256), nn.ReLU(),
            nn.Linear(256, 256), nn.ReLU(),
            nn.Linear(256, 256), nn.ReLU(),
        )
        self.sigma_head = nn.Linear(256, 1)  # Densidade
        self.color_head = nn.Linear(256 + 3*2*dir_enc_dim, 128)  # Cor (depende do ângulo)
        self.color_out = nn.Sequential(nn.Linear(128, 3), nn.Sigmoid())
    
    def positional_encoding(self, x, num_freqs):
        encodings = [x]
        for i in range(num_freqs):
            encodings += [torch.sin(2**i * x), torch.cos(2**i * x)]
        return torch.cat(encodings, dim=-1)
    
    def forward(self, xyz, dirs):
        xyz_enc = self.positional_encoding(xyz, self.pos_enc_dim)
        h = self.net(xyz_enc)
        sigma = F.relu(self.sigma_head(h))
        
        dir_enc = self.positional_encoding(dirs, self.dir_enc_dim)
        color = self.color_out(self.color_head(torch.cat([h, dir_enc], -1)))
        
        return sigma, color
```

### Limitações do NeRF

| Limitação | Impacto |
|---|---|
| Treino lento (horas-dias) | Inviável para aplicações em tempo real |
| Inferência lenta (1+ min/frame) | Não serve para visualização interativa |
| Uma cena por modelo | Não generaliza para novas cenas sem retreinar |
| Qualidade em regiões não vistas | Incerta — só interpola, não extrapola bem |

### Implementação Prática

```bash
# Usar nerfstudio — implementação otimizada moderna
pip install nerfstudio

# Preparar dados com COLMAP
ns-process-data images --data meu_objeto/images/ --output-dir dados_nerf/

# Treinar NeRF
ns-train nerfacto --data dados_nerf/

# Renderizar vídeo de 360°
ns-render camera-path --load-config outputs/...
```

---

## 🔹 BLOCO 6 — 3D GAUSSIAN SPLATTING (ESTADO DA ARTE ATUAL)

> Lançado em 2023. Superou o NeRF em velocidade por 100x+ mantendo qualidade superior. É o que as empresas de XR, metaverso e reconstrução 3D estão usando agora.

> 🛠️ **Nota de validação temporal (esta revisão):** "estado da arte atual" é uma afirmação que envelhece rápido nesta área especificamente. Confirme no momento do seu estudo se Gaussian Splatting continua sendo a abordagem dominante ou se surgiu sucessor relevante — os fundamentos (representação explícita, rasterização ao invés de ray marching) provavelmente continuam valendo como conceito, mesmo que a ferramenta específica mude.

### O Conceito

**Em vez de um MLP pesado, representar a cena como milhões de "bolinhas" (Gaussianas 3D):**

```
Cada Gaussiana tem:
  μ         ← Posição (X, Y, Z) no espaço
  Σ         ← Covariância 3×3 (formato: esférica, achatada, alongada)
  α         ← Opacidade (transparente a sólida)
  SH        ← Spherical Harmonics para cor dependente do ângulo de visão
```

**Splatting:** Para renderizar uma imagem, "espalhar" (splat) cada Gaussiana na câmera 2D e acumular as contribuições — é uma operação muito eficiente na GPU.

### Por que é Rápido?

* NeRF: Para cada pixel, rodar MLP em N pontos = N forward passes
* GS: Rasterizar Gaussianas ordenadas por profundidade = operação GPU paralela

**Resultado:** 100+ FPS de renderização interativa (vs NeRF que levava minutos)

### Treinamento

```
1. Sparse point cloud (COLMAP) → Inicializar Gaussianas em cada ponto
2. Para cada imagem de treino:
   a. Renderizar cena com Gaussianas atuais
   b. Comparar com foto real (L1 loss + SSIM loss)
   c. Propagar gradiente → ajustar posição, forma, cor, opacidade
3. Densificar: adicionar Gaussianas em regiões com gradiente alto
4. Podar: remover Gaussianas transparentes ou muito grandes
```

### Uso Prático (gsplat / 3D Gaussian Splatting)

```bash
# Instalar
pip install gsplat

# Treinar (após ter saída do COLMAP)
python train.py -s meu_objeto/ -m saida_gaussians/

# Visualizar interativo (WebGL)
python render.py -m saida_gaussians/ --web
```

### Resultado Esperado

* Objeto simples (caixa, estátua): 20-40 min de treino, qualidade foto-realista
* Quarto/ambiente: 1-3h de treino
* Visualização interativa a 100+ FPS no browser

---

## 🔹 BLOCO 7 — GERAÇÃO 3D (FRONTEIRA ATUAL)

> Esta área está evoluindo rapidamente. O objetivo é entender os princípios — as ferramentas mudam a cada 6 meses.

### Text-to-3D (Score Distillation Sampling — SDS)

```
Prompt de texto → ?→ Modelo 3D

Como funciona:
1. Inicializar modelo 3D (NeRF ou Gaussianas) como borrão
2. Renderizar de ângulo aleatório → imagem 2D
3. Passar essa imagem por Stable Diffusion congelado
4. SD julga: "o quanto isso parece com o prompt?"
5. Gradiente de SD → volta para o modelo 3D → ajusta Gaussianas
6. Repetir de vários ângulos
```

**Exemplo de ferramentas:** DreamFusion (Google), MVDream, Wonder3D

### Image-to-3D

```
1 foto → Modelo 3D completo

Como funciona:
- Rede treinada em milhões de pares (foto, modelo 3D)
- Aprende a "alucidar" o que há atrás e embaixo do objeto
```

**Ferramentas:** Zero123, LRM, InstantMesh (state of art em 2024)

```python
# Uso típico com InstantMesh
from huggingface_hub import hf_hub_download

# Uma foto de entrada → reconstrução 3D em segundos
pipe = InstantMeshPipeline.from_pretrained("TencentARC/InstantMesh")
meshes = pipe("foto_objeto.png")
meshes[0].export("objeto_3d.obj")
```

---

## 🧪 PROJETOS OBRIGATÓRIOS (PORTFÓLIO PESADO)

### 1️⃣ Fotogrametria para Nuvem de Pontos 3D

**Objetivo:** Reconstruir objeto da mesa em 3D com câmera de celular

1. Gravar vídeo do objeto (30-60 segundos, dar a volta completa)
2. Extrair frames: `ffmpeg -i video.mp4 -vf fps=2 frames/frame_%04d.jpg`
3. Rodar COLMAP para obter poses das câmeras + sparse cloud
4. Visualizar nuvem de pontos esparsa no Open3D
5. Aplicar DepthAnything para dense depth + criar nuvem densa

### 2️⃣ Seu Quarto em 3D Gaussian Splatting

**Objetivo:** Criar modelo 3D fotorrealista navegável em tempo real

1. Usar saída do projeto anterior (COLMAP)
2. Treinar Gaussian Splatting
3. Exportar visualizador WebGL (rodar no browser)
4. Navegar pelo modelo 3D do quarto em tempo real

### 3️⃣ Depth Estimation Pipeline

**Objetivo:** Sistema que recebe imagem e retorna:
* Mapa de profundidade colorido (DepthAnything)
* Nuvem de pontos 3D interativa (Open3D)
* Segmentação 3D do objeto principal (🆕 reaproveitar SAM/SAM2 da Fase 08, Bloco 9, para segmentar o objeto principal antes de gerar a point cloud densa)

### 4️⃣ Reconstrução de Objeto de Produto

**Objetivo:** Recriar produto (sapato, boneco, caixa) para e-commerce 3D

1. Fotografar objeto em plataforma giratória (ou à mão, dando a volta)
2. COLMAP → poses
3. 3D Gaussian Splatting → modelo fotorrealista
4. Exportar como arquivo visualizável (.ply ou WebGL)

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Coordenadas homogêneas e produto de matrizes
2. Modelo de câmera: intrínseca K + extrínseca [R|t]
3. Projeção de ponto 3D → pixel 2D (implementar)
4. Representações 3D: point cloud, voxel, mesh
5. Visão estéreo: disparidade → profundidade
6. DepthAnything: depth de imagem única
7. Depth map → point cloud (implementar)
8. COLMAP: SfM na prática (seu objeto)
9. ler poses COLMAP em Python
10. Volume Rendering (implementar manual)
11. NeRF: implementar toy MLP
12. NeRF com nerfstudio (objeto real)
13. 3D Gaussian Splatting (objeto real)
14. Visualizador WebGL interativo
15. Geração 3D (conceito + ferramentas)
16. **Projetos de portfólio**

---

## 🚨 ERROS FATAIS NESTA FASE

* Ignorar a matemática da câmera (NeRF e GS viram caixa-preta sem isso)
* Não usar COLMAP antes de NeRF/GS (poses das câmeras são entrada obrigatória)
* Tentar treinar Text-to-3D no PC sem GPU potente — não funciona
* Não visualizar resultados intermediários (nuvem de pontos, poses)

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 12 se:

* [ ] Implementa projeção 3D → 2D matematicamente (código + visualização)
* [ ] Usa COLMAP para extrair poses de câmera de fotos reais
* [ ] Entende volume rendering e como o gradiente flui pelo NeRF
* [ ] Constrói model 3D fotorrealista com GS e visualiza em tempo real
* [ ] Cria pipeline depth → point cloud → visualização 3D interativa


---
