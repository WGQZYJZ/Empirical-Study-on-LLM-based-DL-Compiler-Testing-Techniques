import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 9, 3, stride=1, padding=1)
        self.min = min
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = v2 
        return v3
m = Model()
min = 0
# Inputs to the model
x1 = torch.randn(1, 6, 75, 94)
