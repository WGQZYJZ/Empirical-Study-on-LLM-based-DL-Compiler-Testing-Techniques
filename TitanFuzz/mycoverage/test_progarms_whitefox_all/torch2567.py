import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(48, 28, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v3 = torch.clamp_max(v1, 6)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 48, 123, 60)
