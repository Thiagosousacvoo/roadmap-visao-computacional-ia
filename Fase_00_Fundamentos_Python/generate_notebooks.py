import json
import os

base = r'c:\Desenvolvimento\Especialista em Visão Computacional e IA\Fase_00_Fundamentos_Python'

def nb(titulo, subtitulo, cor1, cor2, celulas):
    header_md = [
        f'<div style="background: linear-gradient(135deg, {cor1} 0%, {cor2} 100%); padding: 30px; border-radius: 12px; margin-bottom: 20px;">\n',
        f'  <h1 style="color: white; margin: 0; font-size: 2em;">{titulo}</h1>\n',
        f'  <p style="color: #d1f2eb; margin: 8px 0 0 0; font-size: 1.1em;">{subtitulo}</p>\n',
        '</div>'
    ]
    cells = [{'cell_type':'markdown','metadata':{},'source': header_md}]
    for c in celulas:
        cells.append(c)
    return {
        'cells': cells,
        'metadata': {'kernelspec': {'display_name':'Python 3','language':'python','name':'python3'},'language_info': {'name':'python','version':'3.11.0'}},
        'nbformat': 4,
        'nbformat_minor': 5
    }

def md(src): return {'cell_type':'markdown','metadata':{},'source': src if isinstance(src,list) else [src]}
def code(src): return {'cell_type':'code','execution_count':None,'metadata':{},'outputs':[],'source': src if isinstance(src,list) else [src]}

notebooks = {
    # Bloco 02
    'Bloco_02_Python_Intermediario/02_funcoes_ordem_superior.ipynb': nb(
        '🔗 02 — Funções de Ordem Superior','Fase 00 · Bloco 02','#198754','#20c997',[
        md(['## 🎯 Objetivos\n','\n','- `enumerate()`, `zip()`, `map()`, `filter()`\n','- Substituir loops por operações funcionais\n','\n---\n']),
        code(['# enumerate: índice + valor\n','modelos = ["ResNet", "VGG", "EfficientNet"]\n','for i, nome in enumerate(modelos, start=1):\n','    print(f"{i}. {nome}")']),
        code(['# zip: combinar iteráveis\n','nomes    = ["ResNet", "VGG", "EffNet"]\n','acuracias = [0.932, 0.914, 0.951]\n','params_M  = [25.6, 138.4, 5.3]\n','\n','for nome, acc, params in zip(nomes, acuracias, params_M):\n','    print(f"{nome:12} acc={acc:.3f} params={params}M")']),
        code(['# map: aplicar função a cada elemento\n','def normalizar_acc(acc): return f"{acc:.1%}"\n','\n','acuracias = [0.932, 0.914, 0.951, 0.887]\n','em_pct = list(map(normalizar_acc, acuracias))\n','print(em_pct)']),
        code(['# filter: manter elementos que satisfazem condição\n','modelos = [\n','    {"nome": "ResNet50", "acc": 0.932, "params": 25.6},\n','    {"nome": "VGG16", "acc": 0.914, "params": 138.4},\n','    {"nome": "EffNetB0", "acc": 0.951, "params": 5.3},\n',']\n','\n','# Modelos com acc >= 0.92\n','bons = list(filter(lambda m: m["acc"] >= 0.92, modelos))\n','for m in bons:\n','    print(f"{m[\'nome\']} — {m[\'acc\']:.3f}")']),
        md(['## ✅ Checkpoint\n','\n','- [ ] Uso `enumerate` em vez de `range(len(lista))`\n','- [ ] Uso `zip` para iterar múltiplas listas juntas\n','- [ ] Entendo quando `map`/`filter` é mais claro que list comprehension\n','\n','➡️ **Próximo:** `03_iteradores_e_geradores.ipynb`'])
    ]),
    'Bloco_02_Python_Intermediario/03_iteradores_e_geradores.ipynb': nb(
        '♾️ 03 — Iteradores e Geradores','Fase 00 · Bloco 02','#198754','#20c997',[
        md(['## 🎯 Objetivos\n','\n','- Entender o protocolo iterador (`__iter__`, `__next__`)\n','- Criar geradores com `yield`\n','- Processar dados grandes sem carregar tudo em memória\n','\n---\n']),
        code(['# Iterável vs Iterador\n','lista = [1, 2, 3]\n','iterador = iter(lista)   # Cria iterador a partir da lista\n','\n','print(next(iterador))  # 1\n','print(next(iterador))  # 2\n','print(next(iterador))  # 3\n','# next(iterador)       # StopIteration!']),
        code(['# Gerador: processa um item de cada vez\n','def gerar_batches(dados: list, batch_size: int):\n','    """Gera batches de dados — nunca carrega tudo em memória."""\n','    for i in range(0, len(dados), batch_size):\n','        yield dados[i:i + batch_size]  # yield pausa e retoma\n','\n','dataset = list(range(100))\n','gen = gerar_batches(dataset, batch_size=16)\n','\n','for i, batch in enumerate(gen):\n','    print(f"Batch {i}: {len(batch)} amostras | Primeiro: {batch[0]}, Último: {batch[-1]}")']),
        code(['# Generator expression (lazy)\n','import math\n','\n','# List comprehension — calcula TUDO imediatamente\n','raizes_lista = [math.sqrt(x) for x in range(1_000_000)]  # 1M floats na memória!\n','\n','# Generator expression — calcula UMA DE CADA VEZ\n','raizes_gen = (math.sqrt(x) for x in range(1_000_000))    # Quase sem memória!\n','\n','# Iterar da mesma forma:\n','for raiz in raizes_gen:\n','    if raiz > 5:\n','        print(f"Primeira raiz > 5: {raiz:.4f}")\n','        break']),
        code(['# ✏️ EXERCÍCIO: Gerador de épocas de treino\n','# Implemente gerar_epochs(dados, epochs, batch_size) que:\n','# - Itera epochs vezes sobre os dados\n','# - Gera (epoch_num, batch_num, batch) a cada iteração\n','\n','def gerar_epochs(dados, epochs, batch_size):\n','    # Seu código:\n','    pass\n','\n','dados_fake = list(range(32))\n','for epoch, batch_num, batch in gerar_epochs(dados_fake, epochs=2, batch_size=8):\n','    print(f"E{epoch} B{batch_num}: {batch}")']),
        md(['## ✅ Checkpoint\n','\n','- [ ] Entendo a diferença entre iterável e iterador\n','- [ ] Sei usar `yield` para criar geradores\n','- [ ] Uso generator expressions para grandes datasets\n','\n','➡️ **Próximo:** `04_decorators.ipynb`'])
    ]),
    'Bloco_02_Python_Intermediario/04_decorators.ipynb': nb(
        '🎨 04 — Decorators','Fase 00 · Bloco 02','#198754','#20c997',[
        md(['## 🎯 Objetivos\n','\n','- Entender decorators como wrappers de função\n','- Criar decorator de timing, logging e retry\n','- Usar `functools.wraps` corretamente\n','\n---\n']),
        code(['import time, functools\n','\n','# Decorator básico — medir tempo de execução\n','def medir_tempo(func):\n','    @functools.wraps(func)  # Preserva metadados da função original\n','    def wrapper(*args, **kwargs):\n','        inicio = time.perf_counter()\n','        resultado = func(*args, **kwargs)  # Chama a função original\n','        fim = time.perf_counter()\n','        print(f"  ⏱️ {func.__name__} executou em {(fim - inicio)*1000:.2f}ms")\n','        return resultado\n','    return wrapper\n','\n','@medir_tempo\n','def treinar_epoca(n_amostras: int) -> float:\n','    """Simula treino de uma época."""\n','    soma = sum(i**2 for i in range(n_amostras))\n','    return soma / n_amostras\n','\n','resultado = treinar_epoca(100_000)\n','print(f"Resultado: {resultado:.0f}")']),
        code(['# Decorator com argumento\n','def repetir(n_vezes: int):\n','    """Decorator que repete a função n vezes."""\n','    def decorator(func):\n','        @functools.wraps(func)\n','        def wrapper(*args, **kwargs):\n','            resultados = []\n','            for i in range(n_vezes):\n','                r = func(*args, **kwargs)\n','                resultados.append(r)\n','            return resultados\n','        return wrapper\n','    return decorator\n','\n','@repetir(3)\n','def gerar_predicao() -> float:\n','    import random\n','    return round(random.uniform(0.7, 0.99), 3)\n','\n','predicoes = gerar_predicao()\n','print(f"Predições: {predicoes}")\n','print(f"Média: {sum(predicoes)/len(predicoes):.3f}")']),
        code(['# Decorator de retry — útil para operações de I/O\n','def retry(max_tentativas: int = 3, delay_s: float = 0.1):\n','    """Repete a função até sucesso ou max_tentativas."""\n','    def decorator(func):\n','        @functools.wraps(func)\n','        def wrapper(*args, **kwargs):\n','            for tentativa in range(1, max_tentativas + 1):\n','                try:\n','                    return func(*args, **kwargs)\n','                except Exception as e:\n','                    if tentativa == max_tentativas:\n','                        raise\n','                    print(f"  Tentativa {tentativa} falhou: {e}. Retentando...")\n','                    time.sleep(delay_s)\n','        return wrapper\n','    return decorator\n','\n','import random\n','\n','@retry(max_tentativas=3)\n','def carregar_arquivo_remoto(url: str) -> str:\n','    """Simula download com falha aleatória."""\n','    if random.random() < 0.6:  # 60% de falha\n','        raise ConnectionError(f"Falha ao conectar em {url}")\n','    return f"Conteúdo de {url}"\n','\n','try:\n','    conteudo = carregar_arquivo_remoto("http://exemplo.com/modelo.pth")\n','    print(f"✅ {conteudo}")\n','except Exception as e:\n','    print(f"❌ Falhou após 3 tentativas: {e}")']),
        md(['## ✅ Checkpoint\n','\n','- [ ] Sei criar decorator básico com `*args, **kwargs`\n','- [ ] Uso `@functools.wraps` para preservar docstring e nome\n','- [ ] Crio decorators com parâmetros (factory de decorators)\n','\n','➡️ **Próximo:** `05_type_hints.ipynb`'])
    ]),
    'Bloco_02_Python_Intermediario/05_type_hints.ipynb': nb(
        '📐 05 — Type Hints','Fase 00 · Bloco 02','#198754','#20c997',[
        md(['## 🎯 Objetivos\n','\n','- Anotar tipos em parâmetros, retorno e variáveis\n','- Usar tipos complexos: `list[int]`, `dict[str, float]`, `Optional`\n','- Entender por que type hints melhoram código de IA\n','\n---\n']),
        code(['from typing import Optional, Union\n','import numpy as np  # type: ignore\n','\n','# Type hints básicos\n','def calcular_acuracia(corretos: int, total: int) -> float:\n','    return corretos / total\n','\n','# Optional: parâmetro pode ser None\n','def carregar_modelo(caminho: str, device: Optional[str] = None) -> dict:\n','    """Carrega modelo de arquivo."""\n','    device = device or "cpu"\n','    return {"caminho": caminho, "device": device}\n','\n','# Union: aceita múltiplos tipos\n','def preprocessar(imagem: Union[str, list]) -> list:\n','    if isinstance(imagem, str):\n','        return [0.0]  # Simular leitura de arquivo\n','    return imagem\n','\n','print(calcular_acuracia(89, 100))\n','print(carregar_modelo("modelo.pth"))\n','print(carregar_modelo("modelo.pth", device="cuda"))']),
        code(['# Tipos modernos (Python 3.10+): usar | ao invés de Union\n','def processar(x: int | float | None = None) -> str:\n','    if x is None:\n','        return "nulo"\n','    return f"{x:.4f}"\n','\n','# list, dict, tuple built-ins (sem import em Python 3.9+)\n','def calcular_media(valores: list[float]) -> float:\n','    return sum(valores) / len(valores)\n','\n','def contar_classes(labels: list[str]) -> dict[str, int]:\n','    contagem: dict[str, int] = {}\n','    for l in labels:\n','        contagem[l] = contagem.get(l, 0) + 1\n','    return contagem\n','\n','print(contar_classes(["gato", "cão", "gato", "pássaro"]))']),
        code(['# TypeAlias — criar tipos semânticos\n','from typing import TypeAlias\n','\n','BoundingBox: TypeAlias = tuple[int, int, int, int]  # x1, y1, x2, y2\n','Imagem:      TypeAlias = list[list[list[int]]]       # H x W x C (antes do NumPy)\n','Label:       TypeAlias = str\n','Score:       TypeAlias = float\n','Deteccao:    TypeAlias = tuple[Label, Score, BoundingBox]\n','\n','def detectar(imagem: Imagem) -> list[Deteccao]:\n','    """Retorna lista de detecções na imagem."""\n','    # Simulado:\n','    return [\n','        ("pessoa", 0.95, (10, 20, 100, 200)),\n','        ("cão",    0.87, (150, 50, 250, 180))\n','    ]\n','\n','deteccoes = detectar([[[]]])  # Imagem fake\n','for label, score, bbox in deteccoes:\n','    print(f"  {label:8} conf={score:.2f} bbox={bbox}")']),
        md(['## ✅ Checkpoint\n','\n','- [ ] Anoto todos os parâmetros e retornos das minhas funções\n','- [ ] Uso `Optional[X]` (ou `X | None`) para parâmetros opcionais\n','- [ ] Crio TypeAlias para tornar o código mais semântico\n','- [ ] Entendo que type hints são documentação executável\n','\n','➡️ **Próximo:** `Mini_Projeto_Funcoes_Reutilizaveis.ipynb`'])
    ]),
    'Bloco_02_Python_Intermediario/Mini_Projeto_Funcoes_Reutilizaveis.ipynb': nb(
        '🎯 Mini Projeto — Funções Reutilizáveis','Fase 00 · Bloco 02','#198754','#20c997',[
        md(['## 🎯 Objetivo\n','\n','Criar funções reutilizáveis e robustas usando type hints, decorators, e funções de ordem superior.\n','\n---\n']),
        code(['import functools\nimport time\nfrom typing import Callable, Any\n\n# 1. Decorator de timing\ndef timer(func: Callable) -> Callable:\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        res = func(*args, **kwargs)\n        print(f"⏱️ {func.__name__} executou em {time.time()-start:.4f}s")\n        return res\n    return wrapper\n\n@timer\ndef processamento_pesado(n: int) -> int:\n    return sum(i * i for i in range(n))\n\nprint(processamento_pesado(1_000_000))'])
    ]),

    # Bloco 03
    'Bloco_03_POO/01_classes_e_instancias.ipynb': nb(
        '🏗️ 01 — Classes e Instâncias','Fase 00 · Bloco 03','#fd7e14','#ffc107',[
        md(['## 🎯 Objetivos\n','\n','- Criar classes simples\n','- Instanciar objetos\n','- Construtores (`__init__`) e o `self`\n','\n---\n']),
        code(['class Modelo:\n    def __init__(self, nome: str, acuracia: float):\n        self.nome = nome\n        self.acuracia = acuracia\n\n    def exibir(self):\n        print(f"Modelo: {self.nome} | Acc: {self.acuracia}")\n\nm1 = Modelo("ResNet50", 0.95)\nm1.exibir()'])
    ]),
    'Bloco_03_POO/02_metodos_e_encapsulamento.ipynb': nb(
        '🔒 02 — Métodos e Encapsulamento','Fase 00 · Bloco 03','#fd7e14','#ffc107',[
        md(['## 🎯 Objetivos\n','\n','- Métodos mágicos (`__str__`, `__repr__`)\n','- Encapsulamento (`_protegido`, `__privado`)\n','\n---\n']),
        code(['class Dataset:\n    def __init__(self, caminho: str):\n        self._caminho = caminho\n        self.__dados = [] # privado\n\n    def carregar(self):\n        self.__dados = [1, 2, 3]\n        print(f"Dados carregados de {self._caminho}")\n\n    def __str__(self):\n        return f"<Dataset em {self._caminho} com {len(self.__dados)} itens>"\n\nds = Dataset("/data/train.csv")\nds.carregar()\nprint(ds)'])
    ]),
    'Bloco_03_POO/03_heranca_e_composicao.ipynb': nb(
        '🧬 03 — Herança e Composição','Fase 00 · Bloco 03','#fd7e14','#ffc107',[
        md(['## 🎯 Objetivos\n','\n','- Herança (`class Filha(Pai):`)\n','- `super()`\n','- Composição (usar instâncias de outras classes)\n','\n---\n']),
        code(['class Transform:\n    def aplicar(self, img):\n        pass\n\nclass Resize(Transform):\n    def aplicar(self, img):\n        return f"Resized {img}"\n\nclass Compose:\n    def __init__(self, transforms):\n        self.transforms = transforms\n    \n    def aplicar(self, img):\n        res = img\n        for t in self.transforms:\n            res = t.aplicar(res)\n        return res\n\n# Test\npipeline = Compose([Resize()])\nprint(pipeline.aplicar("imagem.jpg"))'])
    ]),
    'Bloco_03_POO/04_organizacao_de_projeto.ipynb': nb(
        '📂 04 — Organização de Projeto','Fase 00 · Bloco 03','#fd7e14','#ffc107',[
        md(['## 🎯 Objetivos\n','\n','- Como estruturar múltiplos arquivos em um projeto Python\n','- Usar `import` adequadamente\n','\n---\n']),
        code(['# Exemplo estrutural, sem código complexo\n# Em um projeto real:\n# from models.resnet import ResNet\n# from data.dataset import CustomDataset\nprint("Entendido como estruturar diretórios e usar __init__.py!")'])
    ]),
    'Bloco_03_POO/Mini_Projeto_Dataset_Processor_Saver.ipynb': nb(
        '🎯 Mini Projeto — POO em Dados','Fase 00 · Bloco 03','#fd7e14','#ffc107',[
        md(['## 🎯 Objetivo\n','\n','Criar classes para Pipeline de Dados: `Dataset`, `Processor`, `Saver`.\n','\n---\n']),
        code(['class Pipeline:\n    def executar(self):\n        print("Executando pipeline POO completo...")\n\npipeline = Pipeline()\npipeline.executar()'])
    ]),

    # Bloco 04
    'Bloco_04_NumPy/01_arrays_e_criacao.ipynb': nb(
        '🔢 01 — Arrays e Criação','Fase 00 · Bloco 04','#6f42c1','#d63384',[
        md(['## 🎯 Objetivos\n','\n','- Introdução ao NumPy\n','- Criação de Arrays 1D, 2D, 3D\n','\n---\n']),
        code(['import numpy as np\n\narr = np.array([1, 2, 3])\nzeros = np.zeros((2, 2))\nones = np.ones((3, 3))\nprint(arr)\nprint(zeros)\nprint(ones)'])
    ]),
    'Bloco_04_NumPy/02_indexacao_e_slicing.ipynb': nb(
        '🔪 02 — Indexação e Slicing','Fase 00 · Bloco 04','#6f42c1','#d63384',[
        md(['## 🎯 Objetivos\n','\n','- Acesso aos dados do array\n','- Boolean indexing\n','\n---\n']),
        code(['import numpy as np\n\narr = np.arange(10)\nprint(arr[2:5])\nprint(arr[arr > 5])'])
    ]),
    'Bloco_04_NumPy/03_operacoes_vetorizadas.ipynb': nb(
        '🚀 03 — Operações Vetorizadas','Fase 00 · Bloco 04','#6f42c1','#d63384',[
        md(['## 🎯 Objetivos\n','\n','- Operações element-wise\n','- Substituir loops\n','\n---\n']),
        code(['import numpy as np\n\narr = np.array([1, 2, 3])\nprint(arr * 2)\nprint(arr + np.array([4, 5, 6]))'])
    ]),
    'Bloco_04_NumPy/04_broadcasting.ipynb': nb(
        '📡 04 — Broadcasting','Fase 00 · Bloco 04','#6f42c1','#d63384',[
        md(['## 🎯 Objetivos\n','\n','- Entender regras de broadcasting\n','\n---\n']),
        code(['import numpy as np\n\nmatriz = np.ones((3, 3))\nvetor = np.array([1, 2, 3])\nprint(matriz + vetor)'])
    ]),
    'Bloco_04_NumPy/05_algebra_linear.ipynb': nb(
        '📐 05 — Álgebra Linear','Fase 00 · Bloco 04','#6f42c1','#d63384',[
        md(['## 🎯 Objetivos\n','\n','- Dot product\n','- Multiplicação de matrizes\n','\n---\n']),
        code(['import numpy as np\n\nA = np.array([[1, 2], [3, 4]])\nB = np.array([[5, 6], [7, 8]])\nprint(np.dot(A, B))\nprint(A @ B)'])
    ]),
    'Bloco_04_NumPy/06_estatistica.ipynb': nb(
        '📊 06 — Estatística','Fase 00 · Bloco 04','#6f42c1','#d63384',[
        md(['## 🎯 Objetivos\n','\n','- Mean, std, median, percentiles\n','\n---\n']),
        code(['import numpy as np\n\narr = np.random.randn(100)\nprint(f"Média: {np.mean(arr):.4f}")\nprint(f"Desvio: {np.std(arr):.4f}")'])
    ]),
    'Bloco_04_NumPy/07_transformacao.ipynb': nb(
        '🔄 07 — Transformação','Fase 00 · Bloco 04','#6f42c1','#d63384',[
        md(['## 🎯 Objetivos\n','\n','- Reshape, transpose, flatten\n','- Concatenate, stack\n','\n---\n']),
        code(['import numpy as np\n\narr = np.arange(12)\nreshaped = arr.reshape((3, 4))\nprint(reshaped)\nprint(reshaped.T)'])
    ]),

    # Bloco 04.2
    'Bloco_04_2_Pandas/01_dataframe_basico.ipynb': nb(
        '🐼 01 — DataFrame Básico','Fase 00 · Bloco 04.2','#0d6efd','#0dcaf0',[
        md(['## 🎯 Objetivos\n','\n','- Criação e seleção de colunas\n','\n---\n']),
        code(['import pandas as pd\n\ndf = pd.DataFrame({"A": [1, 2], "B": [3, 4]})\nprint(df.head())'])
    ]),
    'Bloco_04_2_Pandas/02_leitura_e_escrita.ipynb': nb(
        '💾 02 — Leitura e Escrita','Fase 00 · Bloco 04.2','#0d6efd','#0dcaf0',[
        md(['## 🎯 Objetivos\n','\n','- `read_csv`, `to_csv`\n','\n---\n']),
        code(['import pandas as pd\n\n# df = pd.read_csv("data.csv")\n# df.to_csv("out.csv", index=False)\nprint("I/O methods ready")'])
    ]),
    'Bloco_04_2_Pandas/03_filtragem.ipynb': nb(
        '🔍 03 — Filtragem','Fase 00 · Bloco 04.2','#0d6efd','#0dcaf0',[
        md(['## 🎯 Objetivos\n','\n','- Filtrar com condições complexas\n','\n---\n']),
        code(['import pandas as pd\n\ndf = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})\nprint(df[df["A"] > 1])'])
    ]),
    'Bloco_04_2_Pandas/04_limpeza_de_dados.ipynb': nb(
        '🧹 04 — Limpeza de Dados','Fase 00 · Bloco 04.2','#0d6efd','#0dcaf0',[
        md(['## 🎯 Objetivos\n','\n','- Tratar nulos e duplicados\n','\n---\n']),
        code(['import pandas as pd\nimport numpy as np\n\ndf = pd.DataFrame({"A": [1, np.nan, 3]})\nprint(df.fillna(0))'])
    ]),
    'Bloco_04_2_Pandas/05_agrupamento_e_agregacao.ipynb': nb(
        '📦 05 — Agrupamento e Agregação','Fase 00 · Bloco 04.2','#0d6efd','#0dcaf0',[
        md(['## 🎯 Objetivos\n','\n','- `groupby`, `agg`\n','\n---\n']),
        code(['import pandas as pd\n\ndf = pd.DataFrame({"Cat": ["A", "A", "B"], "Val": [10, 20, 30]})\nprint(df.groupby("Cat").sum())'])
    ]),

    # Bloco 04.3
    'Bloco_04_3_Matplotlib/01_graficos_basicos.ipynb': nb(
        '📈 01 — Gráficos Básicos','Fase 00 · Bloco 04.3','#fd7e14','#ffc107',[
        md(['## 🎯 Objetivos\n','\n','- Line, scatter, bar, hist plots\n','\n---\n']),
        code(['import matplotlib.pyplot as plt\n\nplt.plot([1, 2, 3], [4, 5, 2])\nplt.show()'])
    ]),
    'Bloco_04_3_Matplotlib/02_imshow_e_imagens.ipynb': nb(
        '🖼️ 02 — Imagens com imshow','Fase 00 · Bloco 04.3','#fd7e14','#ffc107',[
        md(['## 🎯 Objetivos\n','\n','- Visualizar arrays NumPy como imagens\n','\n---\n']),
        code(['import matplotlib.pyplot as plt\nimport numpy as np\n\nimg = np.random.rand(10, 10)\nplt.imshow(img, cmap="gray")\nplt.show()'])
    ]),
    'Bloco_04_3_Matplotlib/03_customizacao_e_subplots.ipynb': nb(
        '🎛️ 03 — Customização e Subplots','Fase 00 · Bloco 04.3','#fd7e14','#ffc107',[
        md(['## 🎯 Objetivos\n','\n','- Labels, titles, subplots\n','\n---\n']),
        code(['import matplotlib.pyplot as plt\n\nfig, axes = plt.subplots(1, 2)\naxes[0].plot([1, 2])\naxes[1].plot([2, 1])\nplt.show()'])
    ]),

    # Bloco 06
    'Bloco_06_Qualidade_de_Codigo/01_complexidade_algoritmica.ipynb': nb(
        '⏱️ 01 — Complexidade Algorítmica','Fase 00 · Bloco 06','#dc3545','#fd7e14',[
        md(['## 🎯 Objetivos\n','\n','- Entender Big O (O(n), O(n²))\n','\n---\n']),
        code(['print("O(n) - Linear")'])
    ]),
    'Bloco_06_Qualidade_de_Codigo/02_codigo_limpo_e_docstrings.ipynb': nb(
        '✨ 02 — Código Limpo e Docstrings','Fase 00 · Bloco 06','#dc3545','#fd7e14',[
        md(['## 🎯 Objetivos\n','\n','- Google Style Docstrings\n','- Variáveis semânticas\n','\n---\n']),
        code(['def limpo(valor: int) -> int:\n    """Multiplica o valor por 2."""\n    return valor * 2'])
    ]),
    'Bloco_06_Qualidade_de_Codigo/03_logging.ipynb': nb(
        '📝 03 — Logging','Fase 00 · Bloco 06','#dc3545','#fd7e14',[
        md(['## 🎯 Objetivos\n','\n','- Substituir print() por logging\n','\n---\n']),
        code(['import logging\n\nlogging.basicConfig(level=logging.INFO)\nlogging.info("Isso é um log profissional.")'])
    ]),

    # Projeto Final
    'Projeto_Final/Exploracao_e_Desenvolvimento.ipynb': nb(
        '🔬 Exploração e Desenvolvimento','Fase 00 · Projeto Final','#212529','#343a40',[
        md(['## 🎯 Objetivos\n','\n','- Explorar os dados do projeto final antes de colocar no main.py\n','\n---\n']),
        code(['import pandas as pd\nimport numpy as np\nprint("Ambiente de exploração pronto!")'])
    ])
}

for path, notebook in notebooks.items():
    full_path = os.path.join(base, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)
    print(f'OK: {path}')

# Add MD files
md_files = {
    'Bloco_05_Ambiente/GUIA_Ambiente_Virtual.md': '# 🌐 Guia de Ambiente Virtual\n\n1. `python -m venv venv`\n2. Ativar\n3. `pip install -r requirements.txt`',
    'Bloco_05_Ambiente/GUIA_Git_Essencial.md': '# 🐙 Guia Git Essencial\n\n- `git init`\n- `git add .`\n- `git commit -m "feat: init"`',
    'Projeto_Final/README.md': '# 🚀 Projeto Final - Pipeline CSV',
    'Projeto_Final/src/dataset.py': 'class Dataset:\n    pass\n',
    'Projeto_Final/src/processor.py': 'class Processor:\n    pass\n',
    'Projeto_Final/src/analysis.py': 'def analyze():\n    pass\n',
    'Projeto_Final/src/utils.py': 'def log():\n    pass\n',
    'Projeto_Final/main.py': 'if __name__ == "__main__":\n    print("Rodando projeto final...")\n'
}

for path, content in md_files.items():
    full_path = os.path.join(base, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'OK: {path}')

print("Todas as pastas e arquivos restantes foram gerados com sucesso!")
