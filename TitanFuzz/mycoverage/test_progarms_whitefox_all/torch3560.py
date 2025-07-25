import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100,1)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.nn.functional.relu(v2)
        return v3

m = Model()
# Initializing the two tensors from the two inputs
x1 = torch.randn(1, 100)
other = torch.randn(1, 1)

