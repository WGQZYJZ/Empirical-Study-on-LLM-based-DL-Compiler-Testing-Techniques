import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, 3, padding=1)
        self.linear = torch.nn.Linear(6, 2)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.linear(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
