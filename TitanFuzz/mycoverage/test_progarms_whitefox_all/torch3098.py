import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
        self.linear = torch.nn.Linear(3, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

m = Model()
# Initializing the model
m = Model(negative_slope=0.125)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
