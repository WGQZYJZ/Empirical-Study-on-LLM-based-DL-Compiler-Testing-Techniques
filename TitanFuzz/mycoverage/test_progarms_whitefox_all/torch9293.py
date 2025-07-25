import torch
from torch import nn

class M1(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + x1
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = M1()

# Inputs to the model
x1 = torch.randn(1, 64)
