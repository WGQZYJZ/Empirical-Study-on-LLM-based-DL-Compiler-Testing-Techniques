import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 32)
 
    def forward(self, x1: torch.Tensor, other: torch.Tensor = None):
        v1 = self.linear(x1)
        v2 = v1 + other
        return F.relu(v2)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
