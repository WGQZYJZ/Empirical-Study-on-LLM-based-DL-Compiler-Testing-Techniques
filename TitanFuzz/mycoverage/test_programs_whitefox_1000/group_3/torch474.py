import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x, out=1):
        out = out + 2
        out = out + x
        return out
m = Model()
# Inputs to the model
x = torch.randn(3, 3, 64, 64)
