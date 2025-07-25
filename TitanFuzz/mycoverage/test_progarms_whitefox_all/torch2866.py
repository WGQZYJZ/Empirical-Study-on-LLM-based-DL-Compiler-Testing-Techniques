import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = torch.mm(input1, input3)
        return input1 + t3 + t2
m = Model()
# Inputs to the model
input1 = torch.randn(1, 3)
input2 = torch.randn(3, 3)
input3 = torch.randn(3, 1)
input4 = torch.randn(1, 3)
