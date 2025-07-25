import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self, min_value=15, max_value=100):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 4, stride=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 4, 3, stride=4)
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = torch.clamp_min(v2, self.min_value)
        v4 = torch.clamp_max(v3, self.max_value)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 511, 511)
