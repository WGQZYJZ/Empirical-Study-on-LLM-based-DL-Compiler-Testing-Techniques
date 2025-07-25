import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Linear(32, 32)
        self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other
        return v2

m = Model()
# Initializing the model
m = Model(torch.randn(1, 32))

# Inputs to the model
x1 = torch.randn(1, 32)
