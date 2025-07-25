import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        t1 = v1.tanh()
        t2 = v1.sigmoid()
        v3 = torch.sigmoid(t1)
        v2 = v1 * v3
        v2 *= v3 * v2 + t2
        v2 *= (v3 + t2 )
        v2 += 320000.0
        v3 = t1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
