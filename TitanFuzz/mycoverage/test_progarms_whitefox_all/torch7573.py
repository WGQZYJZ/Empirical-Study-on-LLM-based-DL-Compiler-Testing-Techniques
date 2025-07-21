import torch
from torch import nn

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, inp)
        v2 = torch.mm(x2, inp)
        return v2 + v1 + inp
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, requires_grad=True)
x2 = torch.randn(1, 1)
inp = torch.randn(1, 1, requires_grad=True)
