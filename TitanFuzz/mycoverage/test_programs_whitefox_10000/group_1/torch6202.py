import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        t1 = torch.rand_like(x)
        t2 = t1 + 1
        return t2
m = Model()
# Inputs to the model
x = torch.rand(3)
