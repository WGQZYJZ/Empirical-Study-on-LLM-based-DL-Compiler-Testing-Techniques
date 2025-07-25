import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, v1)
        v3 = v2 + inp
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(10, 10)
x2 = torch.randn(10, 10)
inp = torch.randn(10, 10)
