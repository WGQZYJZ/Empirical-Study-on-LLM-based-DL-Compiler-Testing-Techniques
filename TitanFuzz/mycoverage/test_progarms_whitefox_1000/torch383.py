import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3, stride=1, padding=1)
    def forward(self, x1):
        v1 = F.relu(x1)
        v2 = self.conv(v1)
        v3 = v2 - 1
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
