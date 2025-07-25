import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self, min_val, max_val):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=min_val)
        v3 = torch.clamp_max(v2, max=max_val)
        return v3

m = Model()
# Initializing the model
m = Model(min_val=-1, max_val=0)

# Inputs to the model
x1 = torch.randn(1, 10)
