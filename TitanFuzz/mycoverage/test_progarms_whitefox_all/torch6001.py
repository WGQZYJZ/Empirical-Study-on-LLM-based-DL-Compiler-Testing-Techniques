import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 16, 3, stride=2)
        self.conv2 = torch.nn.Conv2d(16, 8, 3, stride=2)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 + 0.01
        v3 = F.relu(v2)
        v4 = self.conv2(v3)
        v5 = v4 - 0.74
        v6 = F.relu(v5)
        v7 = torch.squeeze(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
