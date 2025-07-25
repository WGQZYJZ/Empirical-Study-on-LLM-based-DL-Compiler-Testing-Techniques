import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(5, 3, 3, stride=2, groups=3, padding=0)
        self.conv = torch.nn.Conv2d(3, 3, 3, stride=2)
        self.relu = torch.nn.ReLU()
    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        v10 = self.relu(v9)
        v11 = self.conv(v10)
        return v11
m = Model()
# Inputs to the model
x2 = torch.randn(1, 5, 4, 3)
