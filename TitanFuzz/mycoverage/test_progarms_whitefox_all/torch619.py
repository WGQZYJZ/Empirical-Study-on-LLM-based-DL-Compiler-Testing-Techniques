import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2, inp):
        v1 = torch.mm(inp, inp)
        v2 = x2 + v1
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(6, 12)
x2 = torch.randn(12, 6)
inp = torch.randn(12, 12)
