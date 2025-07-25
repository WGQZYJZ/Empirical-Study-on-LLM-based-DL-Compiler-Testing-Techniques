import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose4 = torch.nn.ConvTranspose2d(4, 1, 8, stride=5, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose4(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = v3 / 6
        v5 = v1 * v4
        v6 = v5 / 6
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 10, 10)
