import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, kernel_size=(3, 1), stride=(3, 3), padding=(1, 2), dilation=1, groups=1, bias=False)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - 1.0
        return v2
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 64, 32)
