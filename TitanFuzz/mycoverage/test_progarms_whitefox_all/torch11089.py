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
        v6 = torch.mm(x1, x2)
        v7 = torch.mm(x1, x2)
        v8 = torch.mm(x1, x2)
        v9 = torch.mm(x1, x2)
        v10 = torch.mm(x1, x2)
        v11 = torch.cat([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10], 1)
        return torch.cat([v1, v1, v1, v1, v1, v1, v1, v1, v1, v1, v11], 1)
m = Model()
# Inputs to the model
x1 = torch.randn(2, 1)
x2 = torch.randn(1, 2)
