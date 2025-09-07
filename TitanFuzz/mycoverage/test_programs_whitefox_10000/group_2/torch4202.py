import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2, inp):
        v1 = x1.mm(inp)
        v2 = v1 + x2
        v3 = torch.mm(v1, x2)
        return torch.cat([v2, v3])
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3)
x2 = torch.randn(2, 3)
inp = torch.randn(2, 3)
