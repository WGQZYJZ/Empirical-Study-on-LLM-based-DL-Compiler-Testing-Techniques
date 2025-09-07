import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        t1 = torch.mul(x1, x1)
        return torch.cat([t1, t1, t1], 1)
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3)
