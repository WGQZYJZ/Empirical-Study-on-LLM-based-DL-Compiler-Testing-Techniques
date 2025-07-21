import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        x10 = x * x * x * x * x * x * x * x * x * x
        x11 = x * x * x * x * x * x * x * x * x * x * x * x
        x20 = x * x * x * x
        x21 = x * x * x * x * x * x * x
        return x10 * x20 + x11 * x21
m = Model()
# Inputs to the model
x = torch.randn(8, 8)
