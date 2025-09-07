import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, tensor1):
        t1 = torch.mm(tensor1, tensor1)
        t2 = torch.mm(tensor1, tensor1)
        t3 = torch.mm(tensor1, tensor1)
        t4 = torch.mm(t3, t1)
        t5 = t4 + t2
        return t5
m = Model()
# Inputs to the model
tensor1 = torch.randn(100, 100)
