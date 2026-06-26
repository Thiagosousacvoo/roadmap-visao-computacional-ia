# 🏆 Projeto Final MLOps: SaaS de Visão

Pare de pensar como cientista. Pense como Produto.
Na pasta `Projeto_SaaS_de_Visao` você vai encontrar:

## 1. api.py
Uma API FastApi real. Ela já carrega o modelo YOLO, recebe Upload de Arquivos e retorna o Bounding Box junto com um Log JSON.

## 2. Dockerfile
O ambiente blindado. 

## 3. dashboard.py
O seu painel de comando. Rode `streamlit run dashboard.py` no seu terminal e ele lerá todos os arquivos de Log da API e exibirá gráficos bonitos para te mostrar em tempo real como o seu modelo está performando em produção!
