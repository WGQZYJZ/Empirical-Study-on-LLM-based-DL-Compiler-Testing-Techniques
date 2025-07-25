import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(128, 128)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model(torch.randn(128))

# Inputs to the model
x1 = torch.randn(1, 128)
