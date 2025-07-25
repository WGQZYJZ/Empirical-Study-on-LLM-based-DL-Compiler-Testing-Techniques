import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 3, stride=2, padding=0, dilation=1)
    def forward(self, x):
        v = self.conv_transpose(x)
        v1 = v * 0.5
        v2 = v * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = v1 * v4
        return v5
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 32, 32)
