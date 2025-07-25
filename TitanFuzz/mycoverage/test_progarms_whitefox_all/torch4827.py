import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.a = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.b = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x):
        v1 = self.a(x)
        v2 = self.b(x)
        v3 = v1 - v2
        return v3
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
