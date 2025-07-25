import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = v1 + x1 + x2
        v3 = torch.relu(v2)
        v4 = self.conv1(v3)
        v5 = v4 - x2
        v6 = self.conv1(v5)
        v7 = v6 + x3
        v8 = torch.relu(v7)
        v9 = self.conv2(v8)
        v10 = self.conv1(v9)
        v11 = v10 + x4
        v12 = torch.relu(v11)
        return v12
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 16, 64, 64)
x3 = torch.randn(1, 16, 64, 64)
x4 = torch.randn(1, 16, 64, 64)
