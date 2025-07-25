import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value = 0., max_value = 1.):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)
        
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v1, self.max_value)
        return v3

m = Model()
# Initializing the model
m = Model(0., 1.)

# Inputs to the model
x1 = torch.randn(2, 2)
