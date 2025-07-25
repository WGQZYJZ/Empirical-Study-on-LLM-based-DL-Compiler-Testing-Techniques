import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(3, 5, 1, stride=1, padding=1)
    
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = torch.sigmoid(v1)

        v4 = self.conv2(v3)
        v5 = torch.relu(v4)
        return v1 + v2 + v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
