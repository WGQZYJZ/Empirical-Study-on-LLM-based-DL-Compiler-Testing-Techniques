import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(74, 2, 3, stride=2, bias=False)
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 2, 3, stride=2, output_padding=1, bias=False)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = v2 + 3
        v4 = torch.clamp(v3, min=0)
        v5 = torch.clamp(v4, max=6)
        v6 = v2 * v5
        v7 = v6 / 6
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 74, 17, 21)
