import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min, max):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 12, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(12, 4, 3, stride=1, padding=1)
        self.min = min
        self.max = max
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.clamp_min(v2, self.min)
        v4 = torch.clamp_max(v3, self.max)
        return v4
m = Model()
min = 0.3
max = 0.4
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
