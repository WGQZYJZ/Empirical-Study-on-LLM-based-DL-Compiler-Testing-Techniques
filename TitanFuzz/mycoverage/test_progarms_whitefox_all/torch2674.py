import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = v1 + x2
        v3 = torch.relu(v2)
        v4 = self.conv1(v3)
        v5 = v4 + x2
        v6 = torch.relu(v5)
        v7 = self.conv2(v6)
        v8 = v7 + x2
        v9 = torch.sigmoid(v8)
        return v9
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = 1
