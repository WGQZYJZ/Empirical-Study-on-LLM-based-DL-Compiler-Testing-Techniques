import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 5, stride=1, padding=2)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv(x1)
        v3 = self.conv(x1)
        v4 = self.conv(x1)
        v5 = self.conv(x1)
        v6 = v1 + v2 + v3 + v4 + v5
        v7 = torch.relu(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
