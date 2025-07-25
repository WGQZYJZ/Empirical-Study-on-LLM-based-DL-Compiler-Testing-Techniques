import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_33 = torch.nn.ConvTranspose2d(4, 6, 3, stride=3, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose_33(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
