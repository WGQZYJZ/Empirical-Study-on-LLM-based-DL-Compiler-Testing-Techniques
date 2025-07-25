import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(4, 2, 2, stride=(1, 2), padding=(0, 2))
        self.conv2 = torch.nn.Conv2d(2, 2, 1, stride=1, padding=0)
    def forward(self, x):
        negative_slope = 0.6904382
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v2 > 0
        v4 = v2 * negative_slope
        v5 = torch.where(v3, v2, v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 12, 36)
