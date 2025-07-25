import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, linear):
        super().__init__()
        self.linear = linear
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2

m = Model()
# Initializing the model
linear = torch.nn.Linear(64, 32)
m = Model(linear)

# Inputs to the model
x1 = torch.randn(1, 64)
