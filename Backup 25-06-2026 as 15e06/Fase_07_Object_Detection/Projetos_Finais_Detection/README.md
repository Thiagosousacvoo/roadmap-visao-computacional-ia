# 🏆 Projetos Finais de Detecção: A Vida Real

Chegou a hora de provar que você não é apenas um "Roda-Cadernos".

## Projeto 1: Webcam Tracker Real-Time (O Contador)
Na pasta `Projeto_Webcam_RealTime`, crie um script que:
1. Abra a sua Webcam (usando OpenCV).
2. Passe os frames pelo `model.track()`.
3. Desenhe uma LINHA VIRTUAL no meio da tela.
4. Se a Bounding Box do seu Tracker cruzar a linha, você conta +1.

## Projeto 2: O Treinamento Customizado (Industrial)
Na pasta `Projeto_Treino_Customizado`, você deve:
1. Ir no Roboflow e baixar um dataset real (ex: Carros vs Motos, ou Máscaras).
2. Estruturar a pasta com `data.yaml`.
3. Criar o script de treinamento Python e validar as métricas mAP.
