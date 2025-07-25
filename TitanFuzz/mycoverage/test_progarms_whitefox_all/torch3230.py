import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(64, 32, 3, stride=3, padding=2)
        self.conv2 = torch.nn.Conv2d(32, 8, 1, stride=3, padding=0)
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v2 > 0
        v4 = v2 * -0.025
        v5 = torch.where(v3, v2, v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64, 196, 196)
