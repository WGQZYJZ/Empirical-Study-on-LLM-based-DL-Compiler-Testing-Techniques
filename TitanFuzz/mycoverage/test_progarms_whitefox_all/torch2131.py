import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 6, 4, stride=2, padding=1)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * 0.1
        negative_slope = 100
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 64, 64)
