import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.relu = torch.nn.ReLU()
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + x
        v3 = self.relu(v2)
        return v3
m = Model()
# Inputs to the model
x = torch.randn(1, 16, 64, 64)
