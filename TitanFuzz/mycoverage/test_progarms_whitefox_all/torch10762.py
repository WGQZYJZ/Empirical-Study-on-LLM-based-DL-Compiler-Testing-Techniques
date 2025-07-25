import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1):
        v2 = torch.div(self.conv(x1), 6)
        v3 = torch.clamp_max(v2, 6)
        v4 = torch.clamp_min(v3, 0)
        v5 = v4 + 3
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
