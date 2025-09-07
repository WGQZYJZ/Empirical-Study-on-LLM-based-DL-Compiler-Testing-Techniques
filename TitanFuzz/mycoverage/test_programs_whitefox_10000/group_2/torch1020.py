import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input1):
        t1 = torch.mm(input1, input1)
        return torch.mm(t1, input1)
m = Model()
# Inputs to the model
input1 = torch.randn(5, 5)
