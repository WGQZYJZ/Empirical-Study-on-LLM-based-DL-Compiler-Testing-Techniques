import torch
from torch import nn


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 2)
    def forward(self, x):
        x = torch.matmul(x, self.layers.weight) + self.layers.bias
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
