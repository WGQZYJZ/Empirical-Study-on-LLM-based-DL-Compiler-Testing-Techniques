import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        v3 = torch.mm(x1, x2)
        v4 = torch.mm(x1, x2)
        v5 = torch.mm(x1, x2)
        return torch.cat([v1, v1, v2, v3, v4, v5], 1)
m = Model()
# Inputs to the model
x1 = torch.randn(2, 4)
x2 = 2*torch.randn(4, 1) + torch.randn(4, 1)
