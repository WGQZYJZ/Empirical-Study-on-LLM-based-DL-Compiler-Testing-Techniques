import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        v1 = torch.mm(x, x)
        v2 = torch.mm(x, x)
        return torch.cat([v1, v1, v1, v1, v1, v1, v1, v1, v1, v1, v1, v1, v1], 0)
m = Model()
# Inputs to the model
x = torch.randn(1, 15)
