import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(10, 15, (1, 9), stride=(1, 5), padding=(0, 4))
    def forward(self, x):
        negative_slope = -2.8681044
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 10, 23, 5)
