import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.rand_like(x)
        return x
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
