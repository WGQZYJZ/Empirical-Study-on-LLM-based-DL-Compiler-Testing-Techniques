import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 1
        v3 = v1 * 2
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(2, 8, 32, 32)
