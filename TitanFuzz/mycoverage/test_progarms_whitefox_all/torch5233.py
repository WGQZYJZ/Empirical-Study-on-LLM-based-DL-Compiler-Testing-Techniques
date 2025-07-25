import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        v3 = torch.mm(torch.cat([v1, v2], 1), torch.cat([v1, v2], 1))
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2)
x2 = torch.randn(2, 2)
