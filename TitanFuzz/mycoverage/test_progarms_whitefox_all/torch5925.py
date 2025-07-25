import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 32, 1, stride=1, padding=1)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - torch.ones(1, 32, 64, 64)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 16, 16)
