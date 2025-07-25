import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = v1 * v3
        v5 = v4 / 6
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(5, 1, 64, 64)
