import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(3, 4)
    def forward(self, x):
        x = self.layers(x)
        x = torch.reshape(x, (2, 2))
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3)
