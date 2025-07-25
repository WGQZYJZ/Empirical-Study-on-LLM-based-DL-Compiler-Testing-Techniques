import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv3d(47, 29, (1, 3, 2), stride=(3, 2, 1), padding=3)
    def forward(self, x):
        negative_slope = 0.04982532
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 47, 97, 121, 156)
