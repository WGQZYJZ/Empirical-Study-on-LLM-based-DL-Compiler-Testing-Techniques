import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(8, 16, 3, 1, 0)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, 1, 0)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(x1)
        v4 = torch.sigmoid(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 28, 28)
