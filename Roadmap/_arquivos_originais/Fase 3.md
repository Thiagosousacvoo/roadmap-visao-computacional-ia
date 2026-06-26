Perfeito — essa fase está **muito bem posicionada** na progressão (vem exatamente após ML clássico).  
Agora vou deixar ela **totalmente executável, sem lacunas**, e ajustar alguns pontos que ainda estão implícitos.

---

# **⚠️ PRÉ-REQUISITOS NECESSÁRIOS (ANTES DA FASE 3\)**

## **🔹 Fundamentos**

### **NumPy (nível obrigatório)**

Você precisa dominar:

* Criação de arrays:  
  * `np.array`, `np.zeros`, `np.ones`  
* Indexação:  
  * 1D, 2D, 3D  
* Slicing:  
  * `[linha, coluna]`  
  * `[ :, : ]`  
* Operações vetorizadas:  
  * soma, multiplicação  
* Shape:  
  * `(altura, largura, canais)`

👉 Domínio:

* Manipular matriz SEM usar loop sempre

---

## **🔹 Básico**

### **Álgebra Linear aplicada (mínimo)**

* Vetor \= lista de números  
* Matriz \= grade de números  
* Multiplicação elemento a elemento  
* Produto escalar (para convolução)

---

## **🔹 Intermediário**

### **Python \+ arquivos**

* Ler e salvar arquivos  
* Estruturar projeto

---

## **🔹 Ferramentas obrigatórias**

* OpenCV (`cv2`)  
* NumPy  
* Matplotlib (para debug visual)

---

# **🧱 FASE 3 — VISÃO COMPUTACIONAL (REFINADA E EXECUTÁVEL)**

---

# **🔹 BLOCO 1 — IMAGEM COMO MATRIZ (BASE REAL)**

---

## **📚 Representação de imagem**

### **RGB (3D)**

* Estrutura:  
  * `(altura, largura, canais)`  
  * canais:  
    * 0 → Red  
    * 1 → Green  
    * 2 → Blue

---

### **Grayscale (2D)**

* Estrutura:  
  * `(altura, largura)`

---

## **📚 Acesso a pixels**

### **Indexação**

* `img[y, x]`  
* `img[y, x, canal]`

---

### **Alteração**

* modificar valor direto:  
  * brilho  
  * cor

---

## **📚 Operações básicas**

### **Crop (recorte)**

* `img[y1:y2, x1:x2]`

---

### **Resize**

* `cv2.resize`

---

### **Conversão de cor**

* RGB → Grayscale:  
  * `cv2.cvtColor`

---

## **📚 Escrita e leitura**

* `cv2.imread`  
* `cv2.imwrite`

---

## **🎯 Domínio**

* Tratar imagem como array puro  
* Manipular sem “magia de biblioteca”

---

## **🚧 Exercício obrigatório**

* Ler imagem  
* Converter para grayscale  
* Aumentar brilho manualmente (somar valor nos pixels)  
* Salvar nova imagem

---

# **🔹 BLOCO 2 — CONVOLUÇÃO (BASE DE CNN)**

---

## **📚 Conceito**

### **Kernel**

* matriz pequena:  
  * 3x3  
  * 5x5

---

### **Operação**

* multiplicação local  
* soma dos elementos

---

## **📚 Tipos de filtros**

### **Borda (edge detection)**

* detectar mudanças bruscas

---

### **Blur**

* suavizar imagem

---

### **Sharpen**

* realçar detalhes

---

## **📚 Passo a passo da convolução**

1. Posicionar kernel  
2. Multiplicar elemento a elemento  
3. Somar resultado  
4. Atribuir ao novo pixel

---

## **🛠 Implementação**

### **Manual (OBRIGATÓRIO)**

* usar NumPy  
* percorrer imagem

---

### **Com OpenCV**

* `cv2.filter2D`

---

## **🎯 Domínio**

* Entender:  
  👉 convolução \= operação local

---

## **🚧 Exercício obrigatório**

* Implementar convolução manual (loop controlado)  
* Comparar com OpenCV

---

# **🔹 BLOCO 3 — TÉCNICAS CLÁSSICAS (OPENCV)**

---

## **📚 Detecção de borda**

### **Canny**

* `cv2.Canny`  
* parâmetros:  
  * threshold1  
  * threshold2

---

## **📚 Threshold**

* binarização:  
  * `cv2.threshold`

---

## **📚 Contornos**

* `cv2.findContours`  
* `cv2.drawContours`

---

## **📚 Histogramas**

* distribuição de intensidade  
* `cv2.calcHist`

---

## **📚 Espaço de cor**

### **HSV**

* separar:  
  * Hue  
  * Saturation  
  * Value  
* conversão:  
  * `cv2.cvtColor`

---

## **📚 Transformações geométricas**

### **Translação**

* mover imagem

---

### **Rotação**

* girar imagem

---

### **Escala**

* aumentar/reduzir

---

## **🎯 Domínio**

* Saber escolher técnica para problema simples

---

## **🚧 Mini-projeto BLOCO 3**

* Detector de cor (HSV)

---

# **🔹 BLOCO 4 — VÍDEO**

---

## **📚 Leitura de vídeo**

* `cv2.VideoCapture`

---

## **📚 Processamento de frames**

* loop frame a frame:  
  * `read()`

---

## **📚 Exibição**

* `cv2.imshow`

---

## **📚 Encerramento**

* `cv2.waitKey`  
* `cv2.destroyAllWindows`

---

## **📚 Aplicações**

### **Filtro em tempo real**

* aplicar transformação em cada frame

---

### **Detecção de movimento**

* diferença entre frames:  
  * frame atual vs anterior

---

## **🎯 Domínio**

* Pensar em vídeo como:  
  👉 sequência de imagens

---

## **🚧 Mini-projeto BLOCO 4**

* Detector de movimento simples

---

# **🧪 PROJETOS OBRIGATÓRIOS (DETALHADO)**

---

## **1️⃣ Detector de bordas**

* entrada: imagem  
* saída: imagem com bordas (Canny)

---

## **2️⃣ Detector por cor**

* converter para HSV  
* definir intervalo de cor  
* criar máscara

---

## **3️⃣ Detector de movimento**

* capturar vídeo  
* comparar frames  
* destacar mudança

---

## **4️⃣ Recorte automático**

* detectar região relevante  
* aplicar crop

---

# **⏱ ORDEM EXATA**

1. Imagem como matriz  
2. Leitura/escrita  
3. Manipulação de pixels  
4. Convolução manual  
5. Filtros OpenCV  
6. Canny  
7. Threshold  
8. Contornos  
9. HSV  
10. Transformações  
11. Vídeo  
12. Movimento

---

# **🚨 ERROS QUE VOCÊ DEVE EVITAR**

* Usar OpenCV sem entender matriz  
* Pular convolução manual  
* Só assistir vídeo/aula  
* Não testar com imagens próprias

---

# **✅ CRITÉRIO REAL DE SAÍDA**

Você só passa se:

* Manipula imagem direto com NumPy  
* Explica como filtro funciona  
* Implementa convolução manual  
* Processa vídeo em tempo real  
* Resolve problema simples SEM IA

---

