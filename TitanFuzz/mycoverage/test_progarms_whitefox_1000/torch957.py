import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2, inp):
        v1 = x1.add(inp)
        v2 = x2 - x1
        return v1 * v2
m = Model()
# Inputs to the model
x1 = torch.randn(6, requires_grad=True)
x2 = torch.randn(3, requires_grad=True)
inp = torch.randn(3, requires_grad=True)
