import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.add(3)
        v3 = v2.min(0)
        v4 = v3.min(6)
        v5 = v1.mul(v4)
        v6 = v5.div(6)
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
