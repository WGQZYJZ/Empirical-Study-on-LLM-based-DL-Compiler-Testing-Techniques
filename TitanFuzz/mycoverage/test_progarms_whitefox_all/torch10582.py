import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 8, 3,  padding=1)
        self.conv2 = torch.nn.Conv2d(1, 8, 3,  padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv1(x1)
        v3 = torch.relu(v1 + v2)
        v4 = self.conv2(x1)
        v5 = self.conv2(x1)
        v6 = torch.relu(v4 + v5)
        return torch.cat([v3, v6], dim=1)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
