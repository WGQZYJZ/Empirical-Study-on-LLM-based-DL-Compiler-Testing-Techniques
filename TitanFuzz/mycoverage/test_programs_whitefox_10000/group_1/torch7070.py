import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        t1 = torch.mm(x, x)
        t2 = torch.mm(x, x)
        t3 = t1 * t2
        return t3
m = Model()
# Inputs to the model
x = torch.randn(10, 10)
