import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 4)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 2)
other = torch.tensor(1.0)
