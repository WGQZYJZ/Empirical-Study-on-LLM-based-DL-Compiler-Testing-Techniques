import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 256, kernel_size=1)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - 1.39
        return v2
m = Model()
# Inputs to the model
x = torch.randn(20, 1, 56, 56)
