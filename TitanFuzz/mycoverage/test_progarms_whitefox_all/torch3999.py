import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(212, 197, 3, stride=2, padding=1, dilation=1)
        self.conv2 = torch.nn.Conv2d(197, 70, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(70, 107, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = v7 * 0.5
        v9 = v7 * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8 * v11
        return self.conv3(v12)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 212, 136, 104)
