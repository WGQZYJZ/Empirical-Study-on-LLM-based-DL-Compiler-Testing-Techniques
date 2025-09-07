import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        h2 = torch.mm(x, x)
        h = h2.matmul(h2 - h2)
        return h - torch.mm(x, x)
m = Model()
# Inputs to the model
x = torch.randn(3, 3)
