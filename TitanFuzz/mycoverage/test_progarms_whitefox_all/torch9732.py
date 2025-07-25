import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 30, 5, stride=1, padding=3)
        self.sigmoid = torch.nn.Sigmoid()
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.sigmoid(v1)
        v3 = torch.mul(v1, v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 62, 66)
