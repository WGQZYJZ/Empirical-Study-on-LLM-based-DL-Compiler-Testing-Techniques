import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv1(v1)
        v3 = v2 + v1
        v4 = torch.relu(v3)
        return v4
m = Model()
# Inputs to the model
x = torch.randn(1, 16, 64, 64)
