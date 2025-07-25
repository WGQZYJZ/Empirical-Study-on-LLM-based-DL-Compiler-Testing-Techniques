import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value=-3.7, max_value=-2.2):
        super().__init__()
        self.sqrt = torch.nn.Sqrt()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.sqrt(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
