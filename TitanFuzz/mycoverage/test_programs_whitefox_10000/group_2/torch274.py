import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        return torch.rand_like(x)
m = Model()
# Inputs to the model
x = torch.randn(2)
