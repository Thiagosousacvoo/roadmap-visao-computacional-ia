# 🏆 Projetos Finais: Dominando Pixels

A Fase 08 consolida o mais alto grau técnico clássico. 

## Projeto 1: O "Removedor de Fundo" (CLI)
Na pasta `Projeto_01_Remocao_de_Fundo`, você usará a `torchvision.models.segmentation` (DeepLabV3 ou FCN) pré-treinada para construir uma CLI de extração Alpha.
- Input: `python remove.py --img foto.jpg`
- Output: `foto_recortada.png` (com o fundo transparente!)

## Projeto 2: O Desafio U-Net Médica (Treino Real)
Na pasta `Projeto_02_Treino_UNet_Medica`, você usará a arquitetura U-Net que criamos para um caso real:
1. Vá no Kaggle e procure "Brain Tumor Segmentation".
2. Configure o `dataset.py` com o Data Augmentation Sincronizado.
3. Use **Dice Loss**.
4. Treine por algumas horas e avalie seu IoU.
