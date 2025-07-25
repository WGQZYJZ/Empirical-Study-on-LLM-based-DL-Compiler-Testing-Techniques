import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x4, x4)
        v2 = torch.mm(x1, x3)
        v3 = torch.mm(x4, x2)
        return v1 + v2 + v3
m = Model()
# Inputs to the model
x1 = torch.randn(5, 5)
x2 = torch.randn(5, 5)
x3 = torch.randn(5, 5)
x4 = torch.randn(5, 5)
