import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v = [torch.mm(x1, x2)]
        for loopVar1 in range(1):
            v.append(torch.mm(x1, x2))
        return torch.cat(v, 1)
m = Model()
# Inputs to the model
x1 = torch.randn(4, 10)
x2 = torch.randn(10, 10)
