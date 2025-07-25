import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 3, stride=2, padding=1)
        self.conv2d = torch.nn.Conv2d(8, 32, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v1_48 = self.conv2d(v1)
        v2 = v1_48 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
