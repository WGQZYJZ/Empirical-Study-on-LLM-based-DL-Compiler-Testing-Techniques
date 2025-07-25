import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 2, 3, stride=2, padding=1)
    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5
m = Model()
# Inputs to the model
x2 = torch.randn(8, 4, 64, 64)
