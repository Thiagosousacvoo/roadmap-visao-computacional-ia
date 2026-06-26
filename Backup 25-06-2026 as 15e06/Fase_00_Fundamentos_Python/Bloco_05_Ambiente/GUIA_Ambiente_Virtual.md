# 🌐 Guia Definitivo: Ambiente Virtual (Venv)

> [!IMPORTANT]
> Nunca instale bibliotecas como `numpy`, `pandas` ou `torch` no Python global do seu sistema operativo. Isso causará conflito de versões!

## 1. O que é um Ambiente Virtual?
Um ambiente virtual (`venv`) cria uma pasta isolada no seu projeto com um binário próprio do Python. Se você instalar o OpenCV ali, ele fica ali e não afeta o resto do PC.

## 2. Passo a Passo

### Criando o Ambiente
No terminal (dentro da pasta do projeto):
```bash
python -m venv venv
```
*(O primeiro `venv` é o módulo do Python. O segundo `venv` é o nome da pasta que será criada).*

### Ativando o Ambiente
- **Windows (PowerShell)**: `.\venv\Scripts\Activate.ps1`
- **Linux/Mac**: `source venv/bin/activate`

*Você saberá que funcionou quando o terminal mostrar um `(venv)` no começo da linha.*

### Instalando Dependências
```bash
pip install numpy pandas matplotlib jupyter
```

### Salvando a lista de Dependências
Para que outro dev saiba o que instalar:
```bash
pip freeze > requirements.txt
```
