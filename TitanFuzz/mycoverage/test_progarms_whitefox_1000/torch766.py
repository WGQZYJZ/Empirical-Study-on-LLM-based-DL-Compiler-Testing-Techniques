import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, 1, stride=1, padding=1)
    def forward(self, x1, other=1, padding1=None):
        var1 = self.conv(x1)
        if not padding1 is None:
            var1 += padding1
            var2 = var1 + other
        else:
            var2 = var1 + other
            var3 = var2.transpose(2, 1)
        return var3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
