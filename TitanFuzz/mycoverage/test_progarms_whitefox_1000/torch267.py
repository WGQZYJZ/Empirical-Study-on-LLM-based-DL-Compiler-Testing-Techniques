import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 3, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
    def forward(self, x1, other=1, padding1=None):
        var1 = self.conv1(x1)
        if not padding1 is None:
            var1 += padding1
        var2 = self.conv2(var1)
        var3 = var2 + other
        return var3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
