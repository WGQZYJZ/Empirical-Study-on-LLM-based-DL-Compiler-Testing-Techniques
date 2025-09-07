import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        x2 = torch.rand(1, 2, 2)
        x3 = torch.rand_like(x2)
        y1 = x3 * 2.0
        return y1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
