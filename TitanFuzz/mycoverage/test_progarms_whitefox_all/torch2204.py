import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=1, stride=1, padding=1)
        self.softmax = torch.nn.Sigmoid()
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.softmax(x1)
        v3 = x1 - v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 10, 10)
