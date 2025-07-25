import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=2, padding=0)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = 3 + v1
        v3 = torch.clamp(torch.clamp(v2, min=0), max=6)
        v4 = v3 / 6
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
