import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose3d(32, 3, 3, stride=(1, 1, 1), padding=(2, 2, 2))
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 32, 1, 1, 5)
