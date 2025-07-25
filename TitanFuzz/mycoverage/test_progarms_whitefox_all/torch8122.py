import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 64, 1, stride=1, padding=1)
    def forward(self, x3):
        v1 = self.conv1(x3)
        v2 = self.conv1(x3)
        v3 = v1 + v2
        return v3
m = Model()
# Inputs to the model
x3 = torch.randn(1, 3, 64, 64)
