import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(63, 39, 8, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(39, 7, 7, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(7, 45, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(45, 97, 9, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = self.conv3(v7)
        v9 = v8 * 0.5
        v10 = v8 * 0.7071067811865476
        v11 = torch.erf(v10)
        v12 = v11 + 1
        v13 = v9 * v12
        v14 = self.conv4(v13)
        return v14
m = Model()
# Inputs to the model
x1 = torch.randn(1, 63, 23, 39)
