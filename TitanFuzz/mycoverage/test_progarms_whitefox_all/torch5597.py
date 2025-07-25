import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        # Please create a Linear layer using Pytorch public APIs
        self.linear = torch.nn.Sequential()
        
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3

m = Model()
# Initializing the model
m = Model(min_value=0.0, max_value=1.0)

# Inputs to the model
x1 = torch.randn(1, 7, 30, 30)
