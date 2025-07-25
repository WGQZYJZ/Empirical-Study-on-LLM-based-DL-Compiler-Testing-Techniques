import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = F.relu(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
n = 1
x2 = torch.randn(n, 32)
