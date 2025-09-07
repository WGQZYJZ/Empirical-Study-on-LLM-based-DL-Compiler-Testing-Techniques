import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1

m = Model()
# Initializing the model
m = Model()
m.linear.weight = torch.nn.Parameter(torch.rand(32, 16).fill_(1.0))

# Inputs to the model
x1 = torch.rand(4, 16)
