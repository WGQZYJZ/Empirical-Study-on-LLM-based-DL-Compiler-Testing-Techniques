import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 3)
 
    def forward(self, x0):
        v0 = self.linear(x0)
        v1 = torch.sigmoid(v0)
        return v1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x0 = torch.randn(1, 3)
