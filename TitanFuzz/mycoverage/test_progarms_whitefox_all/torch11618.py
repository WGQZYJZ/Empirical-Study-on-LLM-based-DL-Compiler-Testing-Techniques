import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 16, 3, stride=2, padding=1)
    def forward(self, x1):
        v1 = torch.min(x1, 0.8)
        v2 = self.conv_transpose(v1)
        v3 = v2 + 3
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = v5 / 6
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
