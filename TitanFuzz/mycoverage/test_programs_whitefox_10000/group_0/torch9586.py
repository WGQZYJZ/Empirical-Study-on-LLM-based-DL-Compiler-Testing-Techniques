import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 8)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - 0.7
        v3 = F.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(8, 64)
