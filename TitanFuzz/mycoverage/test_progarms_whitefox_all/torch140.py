import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 0, stride=1, padding=0, groups=1, dilation=1, output_padding=0, bias=True)
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
