import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(10, 20, 3, stride=2, padding='valid')
        self.min = min
        self.max = max
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3
m = Model()
min = 0.4
max = 0.6
# Inputs to the model
x1 = torch.randn(1, 10, 100, 100)
