import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(8)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        v3 = v2 + 3
        v4 = v3.clamp(min=0, max=6)
        v5 = v4.div(6)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
