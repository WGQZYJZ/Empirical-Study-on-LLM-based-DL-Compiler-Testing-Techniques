import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 4, stride=2, padding=1, dilation=2)
        self.conv2 = torch.nn.Conv2d(6, 6, 4, stride=4, padding=1, dilation=2)
    def forward(self, x2):
        v1 = self.conv1(x2)
        v2 = self.conv2(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2
        v5 = v4 * v2
        v6 = v5 * 0.044715
        v7 = v2 + v6
        v8 = v7 * 0.7978845608028654
        v9 = torch.tanh(v8)
        v10 = v9 + 1
        v11 = v3 * v10
        return v11
m = Model()
# Inputs to the model
x2 = torch.randn(1, 3, 32, 32)
