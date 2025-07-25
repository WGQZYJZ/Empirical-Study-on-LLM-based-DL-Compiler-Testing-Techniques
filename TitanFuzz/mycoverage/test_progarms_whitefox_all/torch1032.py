import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(7, 32)
 
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2

m = Model()
# Initializing the model
other = torch.rand(32)
m = Model(other)

# Inputs to the model
x1 = torch.randn(32, 7)
