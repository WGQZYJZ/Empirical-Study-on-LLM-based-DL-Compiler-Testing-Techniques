import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input):
        t1 = torch.mm(input, input)
        t2 = torch.mm(input, input)
        t3 = torch.mm(input, input)
        t4 = torch.mm(input, input)
        t5 = t1 + t2 + t3 + t4
        return t5
m = Model()
# Inputs to the model
input = torch.randn(2, 2)
