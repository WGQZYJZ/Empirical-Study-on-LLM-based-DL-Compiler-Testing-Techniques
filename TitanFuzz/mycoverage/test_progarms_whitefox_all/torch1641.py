import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 5)
        self.other = torch.nn.Parameter(torch.randn(5, 128))
 
    def forward(self, x1):
        v2 = self.linear(x1) + self.other
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 128)
