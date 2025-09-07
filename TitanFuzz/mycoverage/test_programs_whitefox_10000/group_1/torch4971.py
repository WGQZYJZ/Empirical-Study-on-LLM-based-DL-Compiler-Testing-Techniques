import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self,):
        super().__init__()
        self.linear = torch.nn.Linear(16, 16)
 
    def forward(self, input, min_value=-0.1, max_value=0.1):
        v1 = self.linear(input)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
input = torch.randn(1, 16)
