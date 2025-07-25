import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 9, stride=1, padding=4, dilation=3)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 0.8
        v3 = F.relu(v2)
        v4 = torch.reshape(v3, [-1, 128])
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
