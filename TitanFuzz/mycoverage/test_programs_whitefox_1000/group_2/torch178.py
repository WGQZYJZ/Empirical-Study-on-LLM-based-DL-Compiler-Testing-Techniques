import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(nn.Flatten())
    def forward(self, x):
        x = 0.45 * x * (torch.exp(x) - 1.0)
        return x
m = Model()
# Inputs to the model
x = torch.randn(4, 4)
