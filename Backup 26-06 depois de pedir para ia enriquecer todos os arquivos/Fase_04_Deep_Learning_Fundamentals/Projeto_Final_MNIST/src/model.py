import torch.nn as nn

class MNIST_MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        # TODO: Crie suas camadas escondidas nn.Linear(28*28, ...)
        pass
    def forward(self, x):
        # TODO: Implemente o forward
        pass
