import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(64, 64, 1, stride=2, padding=1)
    def forward(self, x1):
        v0 = self.conv(x1)
        v1 = F.relu(v0)
        v2 = v1 - v0
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64, 32, 32)
