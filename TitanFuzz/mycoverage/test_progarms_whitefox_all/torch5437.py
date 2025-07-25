import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, 3, stride=1, padding=1, dilation=1, groups=1, bias=True)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - 1.0
        return v2
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 64, 64)
