import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_9 = torch.nn.ConvTranspose3d(21, 13, 2, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose_9(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 21, 24, 24, 24)
