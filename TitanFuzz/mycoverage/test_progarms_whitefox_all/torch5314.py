import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_12 = torch.nn.ConvTranspose2d(321, 136, 4, stride=1, padding=2, dilation=1)
    def forward(self, x1):
        v1 = self.conv_transpose_12(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 321, 104, 104)
