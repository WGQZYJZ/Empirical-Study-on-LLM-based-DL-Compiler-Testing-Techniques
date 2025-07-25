import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, input1, input2, input3, input4):
        tt = torch.mm(input1, input4)
        t1 = torch.mm(input2, input4)
        t2 = torch.mm(input3, input4)
        t3 = t1 + t2 + tt
        return t3
m = Model()
# Inputs to the model
input1 = torch.randn(4, 3)
input2 = torch.randn(3, 2)
input3 = torch.randn(2, 4)
input4 = torch.randn(4, 3)
