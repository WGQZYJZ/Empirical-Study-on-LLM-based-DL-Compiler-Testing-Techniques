import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v = []
        for i in range(10):
            v += [torch.mm(x1, x2)]
        return torch.cat(v, 1)   
m = Model()
# Inputs to the model
x1 = torch.randn(2, 1)
x2 = torch.randn(1, 3)
