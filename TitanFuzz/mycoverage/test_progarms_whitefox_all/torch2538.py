import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(10, 100)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - self.other
        return v2

m = Model()
# Initializing the model with other
m = Model(torch.tensor([1]))

# Inputs to the model
x1 = torch.randn(1, 10)
