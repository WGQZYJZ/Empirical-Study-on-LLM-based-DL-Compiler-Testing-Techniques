import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, x1, other=None):
        if other is None:
            other = torch.zeros(4)
 
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = v2.clamp(min=0.0)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 4)
