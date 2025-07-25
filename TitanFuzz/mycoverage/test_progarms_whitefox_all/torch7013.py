import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input1, input2, input3):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input1, input3)
        t3 = t2 + t1
        return t2 + t3
m = Model()
# Inputs to the model
input1 = torch.randn(2, 1000)
input2 = torch.randn(1000, 2000)
input3 = torch.randn(1, 2000)
