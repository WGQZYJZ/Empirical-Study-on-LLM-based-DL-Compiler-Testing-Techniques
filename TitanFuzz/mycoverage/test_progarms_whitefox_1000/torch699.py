import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 2, 3)
        self.pool = torch.nn.AvgPool2d(3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.pool(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
