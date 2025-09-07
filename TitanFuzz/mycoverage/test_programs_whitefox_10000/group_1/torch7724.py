import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x, y):
        v1 = torch.mm(x, y)
        out = torch.mm(y, x)
        return v1 + out
m = Model()
# Inputs to the model
x = torch.rand(5, 5)
y = torch.rand(5, 5)
