import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = t1 + 3
        t3 = t2.clamp(min=0, max=6)
        t4 = torch.clamp(t3, 0, 6)
        t5 = t4 / 6
        return t5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
