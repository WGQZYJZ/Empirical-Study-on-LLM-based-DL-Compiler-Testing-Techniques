import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(5, 9, 1, stride=1, padding=1)
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other == None:
            other = torch.randn(1, 9, 64, 64)
        v2 = v1 + other
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 5, 64, 64)
