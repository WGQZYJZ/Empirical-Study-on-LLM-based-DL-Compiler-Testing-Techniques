import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value=4.5, max_value=-0.5):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.conv = torch.nn.Conv2d(8, 3, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.conv(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
