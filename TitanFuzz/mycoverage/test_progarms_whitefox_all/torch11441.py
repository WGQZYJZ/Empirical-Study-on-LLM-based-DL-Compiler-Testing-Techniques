import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(26, 14, 1, stride=2, padding=0, bias=False)
        self.conv2 = torch.nn.Conv2d(14, 20, 5, stride=1, padding=2, bias=False)
        self.conv3 = torch.nn.Conv2d(20, 11, 5, stride=2, padding=2, bias=True)
        self.conv4 = torch.nn.Conv2d(11, 24, 1, stride=1, padding=0, bias=False)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = self.conv3(v7)
        v9 = self.conv4(v8)
        return v9
m = Model()
# Inputs to the model
x1 = torch.randn(1, 26, 94, 94)
