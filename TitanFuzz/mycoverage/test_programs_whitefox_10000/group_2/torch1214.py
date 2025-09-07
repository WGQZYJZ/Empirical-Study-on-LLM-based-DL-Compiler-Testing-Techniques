import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 5)
 
    def forward(self, x):
        v = self.linear(x)
        return v

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 4)
