import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=50, out_channels=27, kernel_size=1, stride=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 50, 16, 16)
