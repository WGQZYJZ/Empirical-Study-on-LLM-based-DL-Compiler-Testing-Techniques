import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 3)
        self.layers2 = nn.Sequential(self.layers, self.layers)
    def forward(self, x):
        x = self.layers2(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
