import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, inp):
        v1 = torch.mm(inp, inp)
        return v1
m = Model()
# Inputs to the model
inp = torch.randn(100000, 1, requires_grad=True)
