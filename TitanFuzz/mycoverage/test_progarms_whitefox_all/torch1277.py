import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 4, kernel_size=3, stride=1, padding=0)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * 0.25
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 60, 30)
