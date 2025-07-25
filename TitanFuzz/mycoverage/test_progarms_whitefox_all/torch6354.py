import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2, x3, inp, v0):
        v1 = torch.mm(x1, x2)
        v3 = torch.mm(x1, x2)
        v2 = torch.mm(v1 + v3, x3)
        v4 = v2 + v1
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3)
x2 = torch.randn(3, 3)
x3 = torch.randn(3, 3)
inp = torch.randn(3, 3)
v0 = torch.randn(3, 3, requires_grad=True)
