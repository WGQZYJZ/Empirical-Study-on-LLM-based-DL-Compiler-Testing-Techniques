import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu6 = torch.nn.ReLU6()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.relu6(self.conv(x1))
        v2 = v1 + 3
        v3 = torch.div(v2, 6)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
