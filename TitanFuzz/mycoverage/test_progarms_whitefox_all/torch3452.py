import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = x.view((x.shape[0], -1))
        y = torch.cat([y] * 2, dim=1)
        y = y.view((x.shape[0], -1))
        return y
m = Model()
# Inputs to the model
x = torch.randn(2, 2, 2)
