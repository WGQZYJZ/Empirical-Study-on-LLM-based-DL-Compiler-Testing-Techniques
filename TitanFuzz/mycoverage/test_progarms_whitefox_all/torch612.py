import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(64, 2, 2, stride=2, dilation=2, groups=2)
        self.conv = torch.nn.Conv2d(2, 2, 10, 1, 0)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.conv(v1)
        v3 = torch.sigmoid(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64, 256, 256)
