import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(1, 4, 1, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 32, (2, 1), stride=(2, 1), padding=(0, 0))
    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv_transpose(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 32, 28, 28)
