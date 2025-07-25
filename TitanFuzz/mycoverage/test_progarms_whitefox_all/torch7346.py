import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(64, 8)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = v2.clamp(0, 6)
        v4 = v3.div(6)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64)
