import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.clamp = torch.nn.ReLU6()
    def forward(self, x1):
        x2 = self.conv(x1)
        x3 = x2 + 3
        x4 = self.clamp(x3)
        x5 = x2 * x4
        x6 = x5 / 6
        return x6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
