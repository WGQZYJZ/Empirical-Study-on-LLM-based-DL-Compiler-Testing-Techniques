import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        return torch.cat([torch.mm(x, x) for i in range(4)], 1)
m = Model()
# Inputs to the model
x = torch.randn(4, 4)
