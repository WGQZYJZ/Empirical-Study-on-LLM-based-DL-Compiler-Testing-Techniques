import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        x2 = torch.rand_like(x1)
        x3 = torch.rand_like(x1)
        t = torch.rand_like(x2)
        return x2
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3, 4, 5)
