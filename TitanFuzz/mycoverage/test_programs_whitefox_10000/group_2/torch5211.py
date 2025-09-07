import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        t = torch.ones(1, 1)
        y = t + x
        return x * x + y
m = Model()
# Inputs to the model
x = torch.ones(1, 1)
