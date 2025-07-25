import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=64, out_channels=16, kernel_size=3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv(v4)
        v6 = torch.sigmoid(v5)
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64, 64, 64)
