import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, 56, stride=1, padding=16)
    def forward(self, x1):
        e1 = self.conv(x1)
        e2 = e1 + 3
        e3 = torch.clamp_min(e2, 0)
        e4 = torch.clamp_max(e3, 6)
        e5 = e1 * e4
        e6 = e5 / 6
        return e6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
