import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 2, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(2, 1, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.nn.functional.interpolate(v2, None, 2, 'nearest')
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 112, 112)
