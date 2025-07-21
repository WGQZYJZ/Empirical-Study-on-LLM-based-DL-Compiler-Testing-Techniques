import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        return v1

m = Model()
# Initializing the model
m = Model()

# The tensor to be added to the output of the linear transformation
other = torch.ones(1, 8)

# Inputs to the model
x1 = torch.randn(1, 3)
