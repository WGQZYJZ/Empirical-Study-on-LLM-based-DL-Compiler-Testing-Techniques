import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(128, 128, 15, 2, 7, bias=False, dilation=1, groups=1, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.sinh(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(64, 128, 128)
