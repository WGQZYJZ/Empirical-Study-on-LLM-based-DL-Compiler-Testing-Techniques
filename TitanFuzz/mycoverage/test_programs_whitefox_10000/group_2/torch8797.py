import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        v1 = x * 0.01 + x * 0.01
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
