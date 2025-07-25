import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 9, (1, 15), stride=(2, 3), padding=(0, 2), dilation=(2, 3))
    def forward(self, x):
        negative_slope = -0.44318062
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 236, 1)
