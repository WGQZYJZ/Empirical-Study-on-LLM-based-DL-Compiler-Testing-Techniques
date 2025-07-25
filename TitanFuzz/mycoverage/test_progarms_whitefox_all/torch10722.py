import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value):
        super().__init__()
        self.linear = torch.nn.Linear(8, 5)
        self.min_value = min_value
        
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=self.min_value)
        v3 = torch.clamp_max(v2, max=1.0)
        return v3

m = Model()
# Initializing the model
m = Model(min_value=0.1)

# Inputs to the model
x1 = torch.randn(1, 8)
