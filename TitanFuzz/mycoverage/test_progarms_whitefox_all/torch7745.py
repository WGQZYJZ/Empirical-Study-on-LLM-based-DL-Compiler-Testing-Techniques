import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input1, input3)
        t2 = torch.mm(input3, input2)
        t3 = torch.mm(input3, input2)
        t4 = torch.mm(input2, input1)
        return t1 + t2 + t3 + t4
m = Model()
# Inputs to the model
input1 = torch.randn(8, 8)
input2 = torch.randn(8, 8)
input3 = torch.randn(8, 8)
input4 = torch.randn(8, 8)
