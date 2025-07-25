import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) + x1
        return v1 ** 2
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3)
inp = torch.randn(3, 3)
