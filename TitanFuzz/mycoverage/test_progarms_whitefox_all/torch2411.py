import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(32, 96, 3, stride=1, padding=2, groups=32)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.sigmoid()
        v3 = v1 * v2
        return v1, v2, v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
