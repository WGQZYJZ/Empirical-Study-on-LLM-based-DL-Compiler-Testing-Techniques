import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input):
        t1 = torch.mm(input, input)
        t2 = t1.mm(input)
        t3 = t1 + t2
        return t2
m = Model()
# Inputs to the model
input = torch.randn(3, 3)
