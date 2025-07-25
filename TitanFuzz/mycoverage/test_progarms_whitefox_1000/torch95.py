import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 256, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(256, 256, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(256, 256, 1, stride=1, padding=1)
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 32, 32)
