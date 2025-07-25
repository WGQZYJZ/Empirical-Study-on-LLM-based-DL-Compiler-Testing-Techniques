import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input):
        t1 = torch.mm(input, input)
        t2 = torch.mm(input, input)
        t3 = torch.mm(input, input)
        t4 = t1 + t3
        return t2 + t4
m = Model()
# Inputs to the model
input = torch.randn(8, 8)
