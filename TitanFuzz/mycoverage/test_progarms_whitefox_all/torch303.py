import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x3)
        v3 = v1 + v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(2, 5)
x2 = torch.randn(5, 3)
x3 = torch.randn(2, 5)
