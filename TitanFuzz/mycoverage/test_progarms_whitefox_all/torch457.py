import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
        self.other = other
m = Model()
# 
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        v3 = F.relu(v2)
        return v3

# Initializing the model
other = torch.randn(1, 16)
m = Model(other=other)

# Inputs to the model
x1 = torch.randn(1, 32)
