import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x, y):
        return torch.mm(x, y)
m = Model()
# Inputs to the model
x = torch.randn(1, 2)
y = torch.randn(2, 1)
