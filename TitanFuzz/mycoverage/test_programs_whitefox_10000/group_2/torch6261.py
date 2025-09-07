import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1):
        x2 = x1.permute(0, 2, 1)
        return x1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
