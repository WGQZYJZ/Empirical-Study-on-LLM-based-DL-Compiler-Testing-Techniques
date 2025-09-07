import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input):
        output = torch.mm(input, input.transpose(0, 1))
        return output + torch.mm(input.transpose(0, 1), input)
m = Model()
# Inputs to the model
input = torch.randn(100, 100)
