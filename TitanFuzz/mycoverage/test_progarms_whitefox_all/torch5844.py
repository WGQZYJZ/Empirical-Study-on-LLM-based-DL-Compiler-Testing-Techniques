import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x1)
        v2 = torch.mm(x2, x2)
        return torch.cat([v1, v1, v2, v2], 1)
m = Model()
# Inputs to the model
x1 = torch.randn(3, 1000)
x2 = torch.randn(1000, 4)
