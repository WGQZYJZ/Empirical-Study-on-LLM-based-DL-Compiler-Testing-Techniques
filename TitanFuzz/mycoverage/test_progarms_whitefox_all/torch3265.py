import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(640, 160, 16, groups=4)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1.tanh()
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 640, 64, 64)
