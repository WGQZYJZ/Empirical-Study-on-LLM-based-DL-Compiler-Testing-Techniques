import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 9, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(9, 9, 1, stride=1, padding=1)
    def forward(self, x):
        negative_slope = -4.36785
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v2 > 0
        v4 = v2 * negative_slope
        v5 = torch.where(v3, v2, v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 21, 18)
