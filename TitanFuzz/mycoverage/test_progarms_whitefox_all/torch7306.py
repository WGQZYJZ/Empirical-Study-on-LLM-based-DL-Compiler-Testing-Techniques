import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1, bias=False)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3

m = Model()
# Initializing the model
m = Model(-300, 300)

# Inputs to the model
x1 = torch.randn(1, 1)
