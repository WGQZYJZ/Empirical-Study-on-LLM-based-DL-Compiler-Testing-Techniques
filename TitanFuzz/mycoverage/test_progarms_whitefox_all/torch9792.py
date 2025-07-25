import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min, max):
        super().__init__()
        self.conv_a = torch.nn.Conv2d(2, 2, 2, stride=1, padding=2)
        self.conv_b = torch.nn.Conv2d(2, 1, 2, stride=1, padding=2)
        self.min = min
        self.max = max
    def forward(self, x1):
        v1 = self.conv_a(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        v4 = self.conv_b(v3)
        return v4
m = Model()
min = 1.75
max = -2.36
# Inputs to the model
x1 = torch.randn(1, 2, 30, 30)
