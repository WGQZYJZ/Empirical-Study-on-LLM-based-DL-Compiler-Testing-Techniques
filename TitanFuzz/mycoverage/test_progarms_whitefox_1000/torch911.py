import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(12, 10, 7, stride=2, bias=False, groups=3, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 12, 4, 4)
