import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = torch.nn.Linear(6, 12, bias=True)(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

m = Model()
# Initializing the model
m = Model(negative_slope=0.1)

# Inputs to the model
x1 = torch.randn(1, 6)
