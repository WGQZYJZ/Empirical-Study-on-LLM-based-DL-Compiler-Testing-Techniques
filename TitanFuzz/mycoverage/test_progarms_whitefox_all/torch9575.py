import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        v0 = torch.mm(x, x)
        v1 = torch.mm(x, x)
        v2 = torch.mm(x, x)
        return v0 + v1 + v2
m = Model()
# Inputs to the model
x = torch.randn(8, 8)
