import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input1):
        return torch.mm(input1, input1 ** 2)
m = Model()
# Inputs to the model
input1 = torch.randn(4, 4)
