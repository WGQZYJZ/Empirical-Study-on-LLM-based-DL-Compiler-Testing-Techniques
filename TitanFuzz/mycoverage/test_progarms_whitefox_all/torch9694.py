import torch
from torch import nn

class ResBlock(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(6, 6)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2

# Initializing the model
other = torch.randn(6)
m = ResBlock(other)

# Inputs to the model
x1 = torch.randn(6)
