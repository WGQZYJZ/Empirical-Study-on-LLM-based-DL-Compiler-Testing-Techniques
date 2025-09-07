import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1):
        a1 = torch.nn.functional.dropout(x1, p=0.2)
        b2 = torch.rand_like(a1)
        return torch.add(a1, b2)
m = Model()
# Inputs to the model
x1 = torch.randn((2, 2))
