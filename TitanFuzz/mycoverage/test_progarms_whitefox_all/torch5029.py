import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 32, 3, stride=1, padding=1)
        self.avg_pool2d = torch.nn.AvgPool2d(3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        v6 = self.avg_pool2d(v5)
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
