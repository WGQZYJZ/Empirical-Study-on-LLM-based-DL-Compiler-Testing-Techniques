import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 - 3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10)
