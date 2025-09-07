import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x, bias=None):
        y1 = F.linear(x, 200, bias=bias)
        y2 = F.linear(x, 200, bias=bias)
        y3 = y1 * y2
        return y3
m = Model()
# Inputs to the model
x = torch.randn(10, 2, 32, 200, dtype=torch.float)
