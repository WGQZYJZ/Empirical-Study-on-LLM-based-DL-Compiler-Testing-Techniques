import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, stride=(21, 21), kernel_size=(15, 15), padding=(14, 14), dilation=4),
    def forward(self, x):
        negative_slope = -24.024891
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 1000, 2000)
