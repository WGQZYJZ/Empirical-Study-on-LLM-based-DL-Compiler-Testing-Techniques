import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x, other):
        v1 = self.linear(x)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 32)
other = torch.randn(2, 16)
