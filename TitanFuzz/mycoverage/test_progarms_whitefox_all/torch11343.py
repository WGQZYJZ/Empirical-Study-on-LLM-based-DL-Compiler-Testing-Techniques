import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(10, 12, 12, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 10, 9, stride=3)
    def forward(self, x48):
        v1 = self.conv1(x48)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        v11 = self.conv2(v10)
        return v11
m = Model()
# Inputs to the model
x48 = torch.randn(1, 10, 23, 12)
