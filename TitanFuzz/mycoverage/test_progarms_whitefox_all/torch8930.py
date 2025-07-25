import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 2, 3, stride=3, padding=3, dilation=3)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 0.5
        v3 = F.relu(v2)
        v4 = self.conv(x1)
        v5 = v4 - 0.5
        v6 = F.relu(v5)
        return v3 + v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
