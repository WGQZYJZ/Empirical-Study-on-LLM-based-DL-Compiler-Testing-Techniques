import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 32, 3, stride=2, padding=1)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.relu(v1)
        v3 = self.conv.weight
        return v2, v3
m = Model()
# Inputs to the model
x = torch.randn(1, 16, 64, 64)
