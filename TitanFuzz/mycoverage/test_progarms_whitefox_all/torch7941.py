import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(6, 4, 5, stride=1, padding=2)
        self.conv = torch.nn.Conv2d(4, 6, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 64, 64)
