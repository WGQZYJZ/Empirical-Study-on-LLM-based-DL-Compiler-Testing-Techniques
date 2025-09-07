import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        x1 = torch.rand_like(x1)
        return x1
m = Model()
# Inputs to the model
x1 = torch.ones(3)
