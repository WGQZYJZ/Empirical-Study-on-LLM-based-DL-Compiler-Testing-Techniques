import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
