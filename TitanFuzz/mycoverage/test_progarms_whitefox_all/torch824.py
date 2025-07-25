import torch
from torch import nn

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(1, 1)
other = torch.randn(1, 1)
