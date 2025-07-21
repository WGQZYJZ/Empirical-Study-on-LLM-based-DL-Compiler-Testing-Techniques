import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input):
        t1 = torch.mm(input, input)
        t2 = torch.mm(input, input)
        return torch.mm(t1, t2)
m = Model()
# Inputs to the model
input1 = torch.randn(1, 1)
