import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 14, 3, stride=1, padding=1)
        self.conv1 = torch.nn.Conv2d(14, 4, 5, stride=1, padding=0, dilation=2)
    def forward(self, x3):
        v1 = self.conv(x3)
        v2 = self.conv1(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2
        v5 = v4 * v2
        v6 = v5 * 0.044715
        v7 = v2 + v6
        v8 = v7 * 0.7978845608028654
        v9 = torch.tanh(v8)
        v10 = v9 + 1
        v11 = v3 * v10
        return v11
m = Model()
# Inputs to the model
x3 = torch.randn(1, 6, 24, 24)
