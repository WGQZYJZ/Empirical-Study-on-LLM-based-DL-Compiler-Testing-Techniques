import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.functional.conv_transpose2d
    def forward(self, x1):
        v1 = self.conv_transpose(input=x1, weight=torch.rand(32, 16, 5, 5), bias=torch.randn(32))
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 256, 256)
