import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input):
        a = torch.mm(input, input)
        b = torch.mm(input, input)
        c = a + b
        return c
m = Model()
# Inputs to the model
input = torch.randn(5, 5)
