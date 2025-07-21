import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input):
        x1 = torch.nn.functional.conv2d(input, weight = torch.tensor(1), bias = torch.tensor(1))[0,0]
        x2 = torch.nn.functional.conv2d(input, weight = torch.tensor(1), bias = torch.tensor(1))[0,0]
        x3 = input[0,0]
        return x1 + x2 - x3
m = Model()
# Inputs to the model
input = torch.randn(1,1,2,2)
