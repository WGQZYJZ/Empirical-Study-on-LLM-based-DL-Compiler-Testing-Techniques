import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_0 = torch.nn.ConvTranspose2d(3, 4096, 7, stride=2, padding=3)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(4096, 4096, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose_0(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose_1(v3)
        v5 = torch.sigmoid(v4)
        v6 = v4 * v5
        v7 = self.conv_transpose_1(v6)
        v8 = torch.sigmoid(v7)
        v9 = v7 * v8
        return v9
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
