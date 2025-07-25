import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 4, 4, stride=2, padding=1)
        # self.flatten = torch.Flatten()
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        # v5[0, :, 1, 1] = -float("inf")
        # v6 = self.flatten(v5)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(4, 16, 32, 32)
