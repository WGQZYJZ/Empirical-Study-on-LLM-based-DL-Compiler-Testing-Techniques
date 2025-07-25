import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 8, 1)
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 - x2
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 4, 5)
x2 = torch.randn(1, 1, 3, 3)
