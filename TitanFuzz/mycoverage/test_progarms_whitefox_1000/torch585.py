import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = v1 + x4
        v3 = torch.relu(v2)
        v4 = self.conv2(v3)
        v5 = torch.nn.functional.interpolate(v4, scale_factor=2, mode='bilinear')
        v6 = v5 + x2
        v7 = torch.relu(v6)
        v8 = torch.nn.functional.interpolate(v7, scale_factor=2, mode='bilinear')
        v9 = v8 + x1
        v10 = torch.relu(v9)
        return v10
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 16, 128, 128)
x3 = torch.randn(1, 16, 64, 64)
x4 = torch.randn(1, 16, 64, 64)
