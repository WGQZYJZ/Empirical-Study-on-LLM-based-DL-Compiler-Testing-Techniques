import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, N, negative_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(N, N, bias=False)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

m = Model()
# Initializing the model
m = Model(4)

# Inputs to the model
x1 = torch.tensor([[1., 2., 3., 4.]])
