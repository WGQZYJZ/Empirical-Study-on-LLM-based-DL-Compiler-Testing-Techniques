import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2

m = Model()
# Initializing the model
p = torch.randn(1, 3)
m = Model(p)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
