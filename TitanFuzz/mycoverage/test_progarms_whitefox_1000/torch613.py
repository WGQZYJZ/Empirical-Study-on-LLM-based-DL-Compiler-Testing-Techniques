import torch
from torch import nn


class Model(torch.nn.Module):
    def forward(self, input):
        f1 = torch.mm(input, torch.transpose(input, 0, 1))
        f2 = torch.mm(input, torch.transpose(input, 0, 1))
        f3 = torch.mm(input, torch.transpose(input, 0, 1))
        return f1 + f2 + f3
m = Model()
# Inputs to the model
x = torch.randn(128, 128)
