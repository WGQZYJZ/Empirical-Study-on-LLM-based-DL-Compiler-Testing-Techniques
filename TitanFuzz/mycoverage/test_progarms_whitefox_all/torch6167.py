import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(6, 8, 2, stride=2, padding=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(8, 16, 2, stride=2, padding=0)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(16, 8, 4, stride=4, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose_2(v3)
        v5 = torch.sigmoid(v4)
        v6 = v4 * v5
        v7 = self.conv_transpose_3(v6)
        v8 = torch.sigmoid(v7)
        v9 = v7 * v8
        return v9
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 32, 32)
