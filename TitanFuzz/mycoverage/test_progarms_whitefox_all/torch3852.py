import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 1, stride=1, padding=1, dilation=1, groups=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 1.0
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 1, 1)
