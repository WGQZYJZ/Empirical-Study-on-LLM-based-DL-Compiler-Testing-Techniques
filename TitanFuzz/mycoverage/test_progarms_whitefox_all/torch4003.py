import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 * clamp(min=0, max=6, v1 + 3)
        v3 = v2 / 6
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 10)
