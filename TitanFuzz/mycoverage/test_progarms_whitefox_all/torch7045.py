import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 6)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + t
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
t = torch.randn(6, 2)
x1 = torch.randn(1, 2)
