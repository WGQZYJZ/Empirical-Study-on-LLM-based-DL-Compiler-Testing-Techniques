import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1, bias=True)
    def forward(self, x1, other=1):
        v1 = self.conv(x1)
        v2 = v1 + other
        v3 = v2.add(other)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
