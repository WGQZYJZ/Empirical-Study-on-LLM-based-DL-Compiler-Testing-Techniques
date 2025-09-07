import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        res = torch.cat([torch.mm(x, x), torch.mm(x, x), torch.mm(x, x)], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        res = torch.cat([res, res], dim=1)
        return res
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
