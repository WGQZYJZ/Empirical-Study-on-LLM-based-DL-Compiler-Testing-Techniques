import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = x2 + v1
        v3 = torch.relu(v2)
        v4 = v1 * x3
        v5 = torch.relu(v4)
        v6 = self.conv2(v5)
        v7 = v3 + v6
        v8 = torch.relu(v7)
        v9 = self.conv3(v8)
        v10 = 1 + v9
        v11 = torch.relu(v10)
        return v11
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 16, 64, 64)
x3 = torch.randn(1, 16, 64, 64)
