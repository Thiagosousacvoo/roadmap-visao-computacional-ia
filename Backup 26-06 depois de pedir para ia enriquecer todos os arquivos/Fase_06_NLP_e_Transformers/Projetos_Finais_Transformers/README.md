# 🏆 Projeto Final Transformers: O Buscador Semântico (CLIP)

Sua missão é sair do jupyter e criar um programa (CLI) de Busca Visual usando a tecnologia CLIP da OpenAI (via Hugging Face).

## O Desafio:
1. Em `data/`, você terá uma pasta cheia de imagens aleatórias (10 a 20 imagens suas).
2. O seu script `indexador.py` deve rodar o CLIP, extrair os Embeddings das 20 imagens e salvar no disco.
3. O seu script `busca.py` deve pedir um input de texto no terminal: `Digite o que procura: `
4. O programa converte o texto para Embedding.
5. Usando "Similaridade de Cosseno", o programa acha a imagem que melhor corresponde ao seu texto livre e exibe na tela!
