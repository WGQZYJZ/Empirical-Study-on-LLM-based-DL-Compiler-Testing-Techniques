import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 5, stride=1, padding=2, bias=False)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 0.4
        v3 = F.relu(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
