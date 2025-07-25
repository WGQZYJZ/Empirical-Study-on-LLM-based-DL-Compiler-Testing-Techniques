import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Conv2d(1, 1, 1, stride=1)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        return v1 + x2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4, 6)
x2 = torch.randn(1, 1, 1, 1)
