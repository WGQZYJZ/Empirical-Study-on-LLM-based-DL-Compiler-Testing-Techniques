import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_20 = torch.nn.ConvTranspose2d(13, 25, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose_20(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 13, 168, 168)
