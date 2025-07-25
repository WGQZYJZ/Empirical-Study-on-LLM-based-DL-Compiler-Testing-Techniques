import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(5, 6, 2)
        self.norm = torch.nn.BatchNorm2d(5, affine=False)
    def forward(self, x):
        x = self.conv(x)
        x = self.norm(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 5, 6, 6)
