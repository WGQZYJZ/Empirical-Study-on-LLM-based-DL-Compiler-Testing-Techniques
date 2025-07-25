import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(6, 10, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(10, 8, 3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v2 - 3
        v4 = F.relu(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 32, 32)
