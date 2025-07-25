import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1):
        x1 = self.conv(x1)
        x1 = x1 + 3
        x1 = torch.clamp_min(x1, 0)
        x1 = torch.clamp_max(x1, 6)
        x1 = torch.div(x1, 6)
        return x1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
