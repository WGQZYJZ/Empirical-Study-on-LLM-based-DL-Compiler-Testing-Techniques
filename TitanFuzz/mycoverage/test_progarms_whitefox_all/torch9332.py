import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, a, b, c):
        d = torch.mm(a, b) + torch.mm(c, c)
        return d
m = Model()
# Inputs to the model
a = torch.randn(17,17)
b = torch.randn(17,17)
c = torch.randn(17,17)
