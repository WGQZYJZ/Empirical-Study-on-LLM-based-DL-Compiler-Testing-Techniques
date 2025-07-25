import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 100)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2
 
m = Model()
# Initializing the model
other = torch.randn(100, 100)
m = Model(other)

# Inputs to the model
x1 = torch.randn(100, 3)
