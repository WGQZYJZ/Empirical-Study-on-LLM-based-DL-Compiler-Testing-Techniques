import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 3, 1, stride=7, padding=0)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(3, 5, 1, stride=11, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        v10 = self.conv_transpose2(v9)
        v11 = 0.9268376703262329 * (v10 * 0.9878847160339355)
        return v11
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 1, 1)
