import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(26, 7, 1, stride=1, padding=2)
    def forward(self, x1, other=0, padding1=0):
        v1 = self.conv(x1)
        if padding1 == 0:
            padding1 = torch.randn(v1.shape)
        v2 = v1 + other
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 26, 16, 16)
