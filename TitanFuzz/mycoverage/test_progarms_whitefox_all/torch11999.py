import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose1 = torch.nn.ConvTranspose2d(8, 8, 3, stride=1, padding=1, dilation=1, groups=8, bias=False)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(1, 5, 3, stride=1, padding=1, dilation=1, groups=1, bias=False)
    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(2, 8, 22, 22)
