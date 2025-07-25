import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(inp, v1)
        v3 = v2 + v1
        v4 = torch.mm(v3, v1)
        v5 = torch.mm(inp, v3)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3, requires_grad=True)
x2 = torch.randn(3, 3, requires_grad=True)
inp = torch.randn(3, 3)
