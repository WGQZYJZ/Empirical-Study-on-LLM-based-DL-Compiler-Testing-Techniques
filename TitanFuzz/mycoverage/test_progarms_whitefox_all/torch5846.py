import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x1, x2, x3, x4):
        a1 = self.conv1(x1)
        v1 = a1 + x1
        v2 = torch.relu(v1)
        v3 = self.conv2(v2) + x2
        v4 = torch.relu(v3)
        v5 = self.conv3(v4) + x3
        v6 = torch.relu(v5)
        v7 = self.conv3(x3)
        v8 = v7 + x4
        v9 = torch.relu(v8)
        return v9
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 16, 64, 64)
x3 = torch.randn(1, 16, 64, 64)
x4 = torch.randn(1, 16, 64, 64)
