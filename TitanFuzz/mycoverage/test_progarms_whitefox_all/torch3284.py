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
        v2 = v1 + x2
        v3 = torch.relu6(v2)
        v4 = self.conv2(v3)
        v5 = v4 + v3
        v6 = torch.relu6(v5)
        v7 = self.conv3(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(2, 16, 64, 64)
x2 = torch.randn(2, 16, 64, 64)
x3 = torch.randn(2, 16, 64, 64)
