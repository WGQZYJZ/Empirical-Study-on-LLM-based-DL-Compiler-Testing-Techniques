import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        return x
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1)
