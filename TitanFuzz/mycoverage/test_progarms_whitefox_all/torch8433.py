import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2
        v3 = x1
        v4 = torch.bmm(v1, v2)
        x11 = v2 * v1
        x12 = v3 * v1
        x13 = v1 * v1
        return x11, x12, x13, v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
