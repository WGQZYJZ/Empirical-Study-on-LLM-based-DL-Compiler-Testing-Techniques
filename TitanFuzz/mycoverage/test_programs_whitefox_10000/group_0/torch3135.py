import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        v1 = torch.mm(x, x)
        v2 = torch.mm(x, v1)
        v3 = torch.mm(x, x)
        return v2 + v3
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
