import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 16, 3, padding=1, stride=2)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.nn.functional.interpolate(v1, [256, 256])
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
