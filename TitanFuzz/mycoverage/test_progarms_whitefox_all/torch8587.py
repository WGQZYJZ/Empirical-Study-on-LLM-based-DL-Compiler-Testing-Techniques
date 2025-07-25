import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)
        self.negative_slope = torch.nn.Parameter(torch.tensor([0.01]))
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        return torch.where(v2, v1, v3)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
