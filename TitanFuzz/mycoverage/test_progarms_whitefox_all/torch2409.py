import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=True)
        
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = v2.relu()
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3)
other = torch.randn(2, 8)
