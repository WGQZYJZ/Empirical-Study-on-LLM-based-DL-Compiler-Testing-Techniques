import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = v2.clamp(min=0)
        v4 = v3 - 3
        v5 = v4.clamp(max=6)
        v6 = v5 / 6
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(5, 3, 64, 64)
