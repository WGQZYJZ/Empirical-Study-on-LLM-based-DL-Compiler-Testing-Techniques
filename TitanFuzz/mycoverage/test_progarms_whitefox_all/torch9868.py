import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
        self.min = min_value
        self.max = max_value
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3

m = Model()
# Initializing the model
m = Model(min_value=-0.5, max_value=0.3)

# Inputs to the model
x1 = torch.randn(1, 5)
