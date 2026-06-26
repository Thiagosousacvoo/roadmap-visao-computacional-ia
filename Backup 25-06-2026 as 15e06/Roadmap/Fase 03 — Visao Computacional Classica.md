# FASE 03 — VISÃO COMPUTACIONAL CLÁSSICA

> **Posição na trilha:** Primeira fase 100% visual. Você aprende a "ver" imagens como dado.
> **Nível:** Intermediário
> **Tempo estimado:** 1 semana (dedicação intensiva de 8–12h/dia)
> **Pré-requisito:** Fase 00 e Fase 01 completas (NumPy sólido é crítico)

---

## ⚠️ PRÉ-REQUISITOS (ANTES DESTA FASE)

### NumPy (nível obrigatório)

* Criação de arrays: `np.array`, `np.zeros`, `np.ones`
* Indexação: 1D, 2D, 3D
* Slicing: `[linha, coluna]`, `[ :, : ]`
* Operações vetorizadas: soma, multiplicação
* Shape: `(altura, largura, canais)`

👉 **Domínio:** Manipular matriz **sem** usar loop sempre

---

### Álgebra Linear aplicada (mínimo)

* Vetor = lista de números
* Matriz = grade de números
* Multiplicação elemento a elemento
* Produto escalar (para convolução)

---

### Ferramentas obrigatórias (instalar antes de começar)

```bash
pip install opencv-python numpy matplotlib
```

* `cv2` (OpenCV) — processamento de imagem
* `numpy` — operações matriciais
* `matplotlib.pyplot` — visualização

---

## 🔹 BLOCO 1 — IMAGEM COMO MATRIZ (BASE REAL)

> Este é o conceito mais importante desta fase: **imagem = array NumPy**. Quando você entende isso, tudo o mais é operação matricial.

### Representação de Imagem

**RGB (3D)**
```
shape: (altura, largura, canais)
canais: 0 → Red, 1 → Green, 2 → Blue
Exemplo: (480, 640, 3)
```

**Grayscale (2D)**
```
shape: (altura, largura)
Exemplo: (480, 640)
```

**Faixa de valores**
* `uint8`: 0 a 255 (padrão)
* `float32`: 0.0 a 1.0 (para redes neurais)

### Acesso a Pixels

```python
img = cv2.imread("foto.jpg")  # Carrega como BGR (não RGB!)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converter para RGB

pixel = img[y, x]          # Valor do pixel (lista de 3 canais)
canal_r = img[y, x, 0]     # Canal R do pixel (x, y)
```

> ⚠️ **Armadilha clássica:** OpenCV carrega imagens em formato **BGR**, não RGB. Sempre converter se for exibir com matplotlib.

### Operações Básicas

**Crop (recorte)**
```python
recorte = img[y1:y2, x1:x2]
```

**Resize**
```python
menor = cv2.resize(img, (320, 240))
# Ou manter aspecto:
escala = 0.5
menor = cv2.resize(img, None, fx=escala, fy=escala)
```

**Conversão de cor**
```python
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
```

**Normalização**
```python
img_float = img.astype(np.float32) / 255.0
```

### Leitura e Escrita

```python
img = cv2.imread("entrada.jpg")
cv2.imwrite("saida.jpg", resultado)
```

### 🎯 Domínio

* Tratar imagem como array puro
* Manipular pixels sem "magia de biblioteca"

### 🚧 Exercício obrigatório

1. Ler imagem com OpenCV
2. Converter BGR → RGB
3. Aumentar brilho manualmente: `img_brilho = np.clip(img + 50, 0, 255).astype(np.uint8)`
4. Recortar região central
5. Salvar nova imagem

---

## 🔹 BLOCO 2 — CONVOLUÇÃO (BASE MATEMÁTICA DE CNN)

> Convolução é a operação central de toda rede neural para imagens. Implementar manualmente aqui é o que vai fazer você entender CNNs de verdade.

### O que é um Kernel (Filtro)

* Matriz pequena (geralmente 3×3 ou 5×5)
* Desliza sobre a imagem
* Em cada posição: multiplicação elemento a elemento + soma = 1 valor

### Operação Formal

```
Para cada posição (i, j) na imagem:
  resultado[i,j] = Σ (vizinhança[i-k, j-l] * kernel[k, l])
```

### Tipos de Filtros e seus Kernels

**Blur (suavização)**
```python
kernel_blur = np.ones((3, 3)) / 9  # Média dos 9 pixels vizinhos
```

**Detecção de borda horizontal (Sobel Y)**
```python
kernel_sobel_y = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
```

**Detecção de borda vertical (Sobel X)**
```python
kernel_sobel_x = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
```

**Sharpen (realce)**
```python
kernel_sharpen = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
```

### Implementação Manual (OBRIGATÓRIO)

```python
def convolver(imagem, kernel):
    """Convoluição manual — sem cv2.filter2D"""
    h, w = imagem.shape
    kh, kw = kernel.shape
    pad = kh // 2
    resultado = np.zeros_like(imagem, dtype=np.float32)
    
    img_padded = np.pad(imagem, pad, mode='constant')
    
    for i in range(h):
        for j in range(w):
            vizinhanca = img_padded[i:i+kh, j:j+kw]
            resultado[i, j] = np.sum(vizinhanca * kernel)
    
    return np.clip(resultado, 0, 255).astype(np.uint8)
```

**Com OpenCV (para comparar):**
```python
resultado = cv2.filter2D(img_gray, -1, kernel)
```

### 🎯 Domínio

* Entender: convolução = operação local que detecta padrão específico
* Saber que CNN aprende os kernels automaticamente (não são fixos)

### 🚧 Exercício obrigatório

1. Implementar convolução manual (código acima)
2. Aplicar kernel de blur, borda e sharpen
3. Comparar resultado manual com `cv2.filter2D` — devem ser idênticos

---

## 🔹 BLOCO 3 — TÉCNICAS CLÁSSICAS COM OPENCV

### Detecção de Borda

**Canny (mais robusto)**
```python
bordas = cv2.Canny(img_gray, threshold1=50, threshold2=150)
```
* `threshold1`: threshold baixo (conecta bordas fracas próximas de fortes)
* `threshold2`: threshold alto (define bordas fortes)

**Sobel (direcional)**
```python
grad_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(grad_x**2 + grad_y**2)
```

### Threshold (Binarização)

```python
_, binario = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Adaptativo (melhor para iluminação variável)
bin_adaptativo = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)
```

### Contornos (Contours)

```python
contours, _ = cv2.findContours(binario, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_cont = img.copy()
cv2.drawContours(img_cont, contours, -1, (0, 255, 0), 2)

# Área e bounding box de cada contorno
for c in contours:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
```

### Histogramas

```python
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title("Histograma de intensidade")
```

### Espaço de Cor HSV (CRÍTICO para detecção por cor)

```python
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Intervalo para detectar cor laranja
lower = np.array([10, 100, 100])
upper = np.array([25, 255, 255])
mascara = cv2.inRange(hsv, lower, upper)
resultado = cv2.bitwise_and(img, img, mask=mascara)
```

**Por que HSV?**
* H (Hue): matiz da cor (0-179 no OpenCV)
* S (Saturation): vivacidade
* V (Value): brilho
* Separar cor de iluminação = filtrar por cor funciona em diferentes luminosidades

### Transformações Geométricas

```python
# Translação
M = np.float32([[1, 0, tx], [0, 1, ty]])
deslocada = cv2.warpAffine(img, M, (w, h))

# Rotação
centro = (w//2, h//2)
M = cv2.getRotationMatrix2D(centro, angulo_graus, escala=1.0)
rotacionada = cv2.warpAffine(img, M, (w, h))

# Flip
espelhada = cv2.flip(img, 1)  # 0=vertical, 1=horizontal, -1=ambos
```

### 🚧 Mini-projeto — BLOCO 3

**Detector de cor em tempo real**
1. Abrir webcam
2. Converter frame para HSV
3. Criar máscara para uma cor específica (laranja, verde, etc.)
4. Exibir frame com máscara aplicada + contorno destacado

---

## 🔹 BLOCO 4 — PROCESSAMENTO DE VÍDEO

> Vídeo = sequência de imagens (frames). Cada frame é um array. O loop de processamento é a base de qualquer sistema de visão em tempo real.

### Leitura de Vídeo

```python
# Webcam
cap = cv2.VideoCapture(0)

# Arquivo de vídeo
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Processar frame aqui
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Resultado", gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Salvar Vídeo

```python
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('saida.mp4', fourcc, fps=30, frameSize=(w, h))

# No loop:
out.write(frame_processado)

out.release()
```

### Detecção de Movimento

```python
frame_anterior = None

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if frame_anterior is None:
        frame_anterior = gray
        continue
    
    diferenca = cv2.absdiff(frame_anterior, gray)
    thresh = cv2.threshold(diferenca, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) < 500:  # Ignorar ruído
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    frame_anterior = gray
```

### 🎯 Domínio

* Pensar em vídeo como: sequência de imagens
* Toda operação de imagem funciona frame a frame
* **Explicitamente necessário na Fase 07 (Object Detection em vídeo)**

### 🚧 Mini-projeto — BLOCO 4

* Detector de movimento com gravação automática quando detecta movimento

---

## 🧪 PROJETOS OBRIGATÓRIOS (DETALHADO)

### 1️⃣ Detector de Bordas

* Entrada: imagem qualquer
* Pré-processar (grayscale + blur)
* Aplicar Canny com threshold ajustável
* Saída: imagem original lado a lado com bordas detectadas

### 2️⃣ Detector por Cor (HSV)

* Converter para HSV
* Definir intervalo de cor com sliders interativos (`cv2.createTrackbar`)
* Criar máscara e highlight da região detectada

### 3️⃣ Detector de Movimento em Vídeo

* Capturar vídeo (webcam ou arquivo)
* Comparar frames consecutivos
* Destacar regiões com mudança
* Contar objetos em movimento com contornos

### 4️⃣ Pipeline de Pré-processamento de Imagem

* Receber imagem de qualquer tamanho e canal
* Normalizar para formato padrão: `(224, 224, 3)`, `float32`, valores 0-1
* Esta é a entrada padrão para redes neurais (preparação para Fase 05)

---

## ⏱ ORDEM EXATA DE EXECUÇÃO

1. Imagem como array (RGB, grayscale, shapes)
2. Acesso a pixels e slicing
3. Conversão de cores (BGR↔RGB, ↔Grayscale, ↔HSV)
4. Operações básicas (crop, resize, flip)
5. **Convolução manual** (loop NumPy)
6. Comparar com `cv2.filter2D`
7. Filtros clássicos (blur, borda, sharpen)
8. Canny e Sobel
9. Threshold (simples e adaptativo)
10. Contornos e bounding boxes
11. Histogramas
12. HSV e detecção por cor
13. Transformações geométricas
14. Vídeo: leitura de webcam
15. Detecção de movimento
16. **Projetos obrigatórios**

---

## 🚨 ERROS QUE VOCÊ DEVE EVITAR

* Usar OpenCV sem entender que é tudo array NumPy por baixo
* Pular a convolução manual (vai doer nas fases de CNN)
* Só assistir vídeo/aula — cada técnica tem que ser testada com imagem própria
* Não testar com imagens próprias (webcam, fotos suas)
* Esquecer de converter BGR → RGB ao usar matplotlib

---

## ✅ CRITÉRIO REAL DE SAÍDA

Você só avança para a Fase 04 se:

* [ ] Manipula imagem diretamente com NumPy (sem OpenCV quando possível)
* [ ] Explica como um filtro de convolução funciona matematicamente
* [ ] Implementa convolução manual que gera resultado igual ao OpenCV
* [ ] Processa vídeo em tempo real com pelo menos uma transformação
* [ ] Resolve problema simples (detecção por cor, detecção de movimento) **sem IA**
* [ ] Constrói pipeline de pré-processamento para formato de entrada de redes neurais
