import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min=0.5, max=0.75):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
        self.min = min
        self.max = max
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
