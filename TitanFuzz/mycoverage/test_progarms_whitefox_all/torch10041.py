import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 1, 2)
        self.conv2 = torch.nn.Conv2d(1, 1, 1)
        self.bn = torch.nn.BatchNorm2d(1)
    def forward(self, x):
        x = self.bn(self.conv1(x))
        x = self.conv2(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 4, 4)
