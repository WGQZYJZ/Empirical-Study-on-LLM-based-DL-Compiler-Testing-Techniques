import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 16, 20, stride=20, padding=0)
        self.min = min
        self.max = max
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3
m = Model()
min = 0.2
max = 0.4
# Inputs to the model
x1 = torch.randn(1, 16, 100, 100)
