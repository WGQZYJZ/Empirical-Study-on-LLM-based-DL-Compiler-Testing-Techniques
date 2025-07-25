import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 256)
 
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = v2.relu()
        return v3

m = Model()
# Initializing the model
m = Model(other=torch.randn(1, 256, 64*64))

# Inputs to the model
x1 = torch.randn(1, 64*64)
