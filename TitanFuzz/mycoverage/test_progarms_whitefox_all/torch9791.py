import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3, stride=1, padding=1)
        self.conv_p = torch.nn.Conv2d(2, 2, 1, stride=1, padding=0)
        self.min = min
        self.max = max
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        v4 = self.conv_p(v3)
        v5 = torch.clamp_min(v4, self.min)
        v6 = torch.clamp_max(v5, self.max)
        return v6
m = Model()
min = 0.05
max = 0.43
# Inputs to the model
x1 = torch.randn(1, 1, 300, 300)
x2 = torch.randn(1, 1, 300, 300)
