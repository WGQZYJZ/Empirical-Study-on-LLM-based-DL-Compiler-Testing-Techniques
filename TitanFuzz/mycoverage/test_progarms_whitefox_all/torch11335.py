import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3, groups=8)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1, groups=4)
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = v1 + x4
        v3 = torch.relu(v2)
        v4 = self.conv2(v3)
        a1 = self.conv1(x3)
        v5 = v4 + a1
        a2 = self.conv2(x1)
        v6 = v5 + a2
        v7 = torch.relu(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 16, 64, 64)
x3 = torch.randn(1, 16, 64, 64)
x4 = torch.randn(1, 16, 64, 64)
