import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 8, 2, stride=1, padding=1)
    def forward(self, x1, other, padding1, padding2=None):
        v1 = self.conv(x1)
        if padding2 == None:
            padding2 = torch.randn(v1.shape)
        v2 = v1 + other
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 48, 64)
