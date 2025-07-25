import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 32, 1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 15
        v3 = F.relu(v2)
        v4 = v3 - self.conv(x1)
        v5 = F.relu(v4)
        v6 = torch.transpose(v3, 0, 2)
        v7 = F.relu(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
