import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(4, 8, 3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv1(x1)
        v3 = self.conv2(v1)
        v4 = self.conv2(v2)
        v5 = v3 + v4
        v6 = torch.relu(v5)
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 60, 60)
