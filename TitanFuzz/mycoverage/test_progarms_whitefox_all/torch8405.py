import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x2, x2)
        v3 = torch.mm(v1, v2)
        v4 = torch.mm(v1, v1)
        v5 = torch.mm(v3, v2)
        t1 = torch.cat([v5, v4], 1)
        return t1
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3)
x2 = torch.randn(3, 2)
