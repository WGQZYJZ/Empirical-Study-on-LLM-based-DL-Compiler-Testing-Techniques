import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(17, 10, 1, stride=1, padding=1, groups=1)
    def forward(self, x1, t1):
        v1 = self.conv(x1)
        v2 = v1 + t1
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(3, 17, 64, 64)
t1 = 1
