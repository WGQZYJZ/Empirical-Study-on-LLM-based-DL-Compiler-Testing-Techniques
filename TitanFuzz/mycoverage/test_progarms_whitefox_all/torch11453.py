import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(3, 32,  bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3

m = Model()
# Initializing the model
m = Model(min_value=-0.5, max_value=0.4)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
