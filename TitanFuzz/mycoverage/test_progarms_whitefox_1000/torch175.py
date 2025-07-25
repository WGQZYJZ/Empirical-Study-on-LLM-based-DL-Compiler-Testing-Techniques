import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(1, 1, kernel_size=(1,), stride=(1,), padding=(0,), dilation=1, groups=1, bias=False)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - x
        return v2
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 64, 64)
