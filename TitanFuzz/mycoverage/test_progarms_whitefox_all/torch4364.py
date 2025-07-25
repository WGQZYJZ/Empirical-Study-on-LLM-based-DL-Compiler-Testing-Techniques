import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 4, 2, stride=2, padding=1)
        self.t1 = torch.nn.Linear(32, 32)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.t1(v1)
        v3 = torch.sigmoid(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
