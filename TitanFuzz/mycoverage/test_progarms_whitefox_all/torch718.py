import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(8, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

m = Model()
# Initializing the model
min_value = 0
max_value = 100
m = Model(min_value, max_value)

# Inputs to the model
x1 = torch.randn(1, 8)
