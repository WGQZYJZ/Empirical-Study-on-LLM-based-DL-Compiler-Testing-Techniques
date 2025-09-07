import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1, x2):
        v1 = torch.mm(x1.T, x2)
        v2 = torch.mm(x1, x2.T)
        v3 = v1 + v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(5, 4)
x2 = torch.randn(4, 3)
