import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 50, 1, stride=1, padding=0)
    def forward(self, x):
        negative_slope = 3.0654767
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 18, 5)
