import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3, bias=False)
        self.bn = torch.nn.BatchNorm2d(3)
    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 3, 3)
