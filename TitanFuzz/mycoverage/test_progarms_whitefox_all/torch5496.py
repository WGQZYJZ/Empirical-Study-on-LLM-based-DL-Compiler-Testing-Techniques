import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 12, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(12, 18, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(12)
        self.bn2 = torch.nn.BatchNorm2d(18)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.bn1(v2)
        v4 = v3 - 3
        v5 = torch.clamp_max(v4, 6)
        v6 = v3 * v5
        v7 = self.bn2(v6)
        v8 = v7 / 3
        return v8
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
