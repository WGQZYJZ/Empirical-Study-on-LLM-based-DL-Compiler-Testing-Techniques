import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(40, 60)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float()
        v3 = 0.1 * v1
        v4 = v1
        v4 = torch.where(v2, v1, v3)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 40)
