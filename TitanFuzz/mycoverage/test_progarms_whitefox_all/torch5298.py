import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(17, 32, 1, stride=1, padding=0)
    def forward(self, x1, other=1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 17, 64, 64)
