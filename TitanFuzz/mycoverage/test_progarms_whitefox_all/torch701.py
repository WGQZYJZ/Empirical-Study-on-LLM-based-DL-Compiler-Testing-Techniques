import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1, other):
        v1 = torch.nn.functional.linear(x1, other)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16)
other = torch.randn(16, 16)
