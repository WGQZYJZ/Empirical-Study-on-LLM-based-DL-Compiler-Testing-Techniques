import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, stride=4):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=stride, padding=1)
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v2 > 0
        v4 = v2 * -0.01
        v5 = torch.where(v3, v2, v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
