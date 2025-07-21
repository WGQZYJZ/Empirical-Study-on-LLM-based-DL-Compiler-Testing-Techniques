import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        return torch.mm(torch.mm(x, x), x)
m = Model()
# Inputs to the model
x = torch.randn(8, 8)
