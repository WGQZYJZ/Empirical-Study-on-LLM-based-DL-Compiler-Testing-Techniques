import torch
from torch import nn


class Model(torch.nn.Module):
    def forward(self, input1):
        mm1 = input1.mm(input1)
        mm2 = input1.mm(input1)
        return mm1 + mm2
m = Model()
# Inputs to the model
input1 = torch.randn(2, 2)
