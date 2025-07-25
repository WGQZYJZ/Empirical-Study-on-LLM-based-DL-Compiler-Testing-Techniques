import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 9, stride=1, padding=4)
    def forward(self, x1):
        v2 = 3 + self.conv(x1)
        v3 = v2.clamp(min=0, max=6)
        v4 = v3 / 6
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
