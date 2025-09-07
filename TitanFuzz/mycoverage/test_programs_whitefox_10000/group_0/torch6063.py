import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input):
        t1 = torch.mm(input, input)
        t2 = torch.mm(input, input)
        t3 = t1 + t2
        return t3
m = Model()
# Inputs to the model
input = torch.randn(8, 8)
