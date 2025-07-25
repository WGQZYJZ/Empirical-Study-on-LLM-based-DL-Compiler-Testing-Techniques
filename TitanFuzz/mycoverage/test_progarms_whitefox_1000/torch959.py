import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 8, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = v1 + v2
        v4 = torch.relu(v3)
        v5 = v1 + v4
        v6 = v2 + v5
        v7 = torch.relu(v6)
        v9 = v1 + v7
        v10 = v2 + v9
        v11 = torch.relu(v10)
        v13 = v1 + v11
        v14 = v2 + v13
        v15 = torch.relu(v14)
        return v15
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
# Model begins
