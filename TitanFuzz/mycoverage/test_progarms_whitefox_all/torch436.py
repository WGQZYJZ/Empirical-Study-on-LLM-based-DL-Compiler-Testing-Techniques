import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 ='str'
        if v2:
            v3 = v1 - 3.5
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
