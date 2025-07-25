import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min, max):
        super().__init__()
        self.conv_0 = torch.nn.Conv2d(12, 80, 11, stride=1, padding=7)
        self.conv_1 = torch.nn.Conv2d(80, 192, 5, stride=1, padding=2)
        self.min = min
        self.max = max
    def forward(self, x1):
        v1 = self.conv_0(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = self.conv_1(v2)
        v4 = torch.clamp_max(v3, self.max)
        return v4
m = Model()
min = 0.1
max = 0.3
# Inputs to the model
x1 = torch.randn(1, 12, 20, 20)
