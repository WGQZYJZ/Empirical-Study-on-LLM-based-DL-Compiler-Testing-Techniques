import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self, min_value=5, max_value=16):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose1d(4, 2, 3)
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 20)
