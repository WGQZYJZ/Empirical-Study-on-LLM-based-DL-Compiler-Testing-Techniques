import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.relu = torch.nn.functional.relu
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.relu(v1)
        v3 = v2 - 0.234
        return v3
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
a = 2.4
