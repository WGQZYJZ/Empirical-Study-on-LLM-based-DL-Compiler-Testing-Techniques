import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 9, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 0.0001
        v3 = F.relu(v2)
        v4 = torch.zeros_like(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 64, 64)

