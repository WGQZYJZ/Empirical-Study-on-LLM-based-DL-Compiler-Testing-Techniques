import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v1 = torch.mm(v1, x2)
        v2 = torch.mm(x1, x2)
        v = v1 + v2
        return torch.cat([v, v, v, v, v, v, v, v], 1)
m = Model()
# Inputs to the model
x1 = torch.randn(512, 2)
x2 = torch.randn(2, 1)
