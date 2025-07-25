import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 16, bias=False)
        
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = v1 + x2
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 64)
x3 = torch.randn(1, 64)
