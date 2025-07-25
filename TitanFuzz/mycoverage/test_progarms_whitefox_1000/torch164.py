import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 8, 3, stride=1, padding=1, dilation=2, groups=4)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * 0.1
        v4 = torch.where(v2, -v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
