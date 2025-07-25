import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input1, input2, input3, input4, input5):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = input5.permute(2, 0, 1)
        t4 = torch.mm(t1, t3)
        return t4
m = Model()
# Inputs to the model
input1 = torch.randn(3, 3, 3)
input2 = torch.randn(3, 3, 3)
input3 = torch.randn(3, 3, 3)
input4 = torch.randn(3, 3, 3)
input5 = torch.randn(3, 3, 3)
