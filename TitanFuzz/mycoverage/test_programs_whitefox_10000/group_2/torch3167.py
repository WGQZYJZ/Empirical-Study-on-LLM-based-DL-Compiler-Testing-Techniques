import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
 
    def forward(self, x, other=None):
        v1 = self.linear(x)
        r2 = v1 + other
        r3 = torch.relu(r2)
        return r3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2)
other = torch.ones(1)
