import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 16, 3)
        self.conv2 = torch.nn.Conv2d(16, 16, 3)
    def forward(self, x1):
        v2 = self.conv2(x1)
        v1 = self.conv1(x1)
        v1 = v1 - v2
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
