import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 32)
        self.linear2 = torch.nn.Linear(32, 32)
 
    def forward(self, x1, other):
        v1 = self.linear1(x1)
        v2 = v1 + other
        v3 = self.linear2(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 32)
other = torch.randn(8, 32)
