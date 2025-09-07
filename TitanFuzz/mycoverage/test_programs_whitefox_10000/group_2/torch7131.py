import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        self.linear = torch.nn.Linear(25, 1,bias=False)
 
    def forward(self, x1):
        h0 = self.linear(x1)
        h1 = h0 - other
        return h1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 13, 13)
other = torch.randn(1)
