import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(8, 8, 2, stride=1, padding=1)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(8, 8, 2, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose_3(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose_4(v3)
        v5 = torch.sigmoid(v4)
        v6 = v4 * v5
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
