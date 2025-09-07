import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(16, 16)
        self.other = other
 
    def forward(self, x):
        v = self.linear(x)
        return v + self.other

m = Model()
# Initializing the model
other = torch.randn(1, 16)
m = Model(other)

# Inputs to the model
x = torch.randn(1, 16)
