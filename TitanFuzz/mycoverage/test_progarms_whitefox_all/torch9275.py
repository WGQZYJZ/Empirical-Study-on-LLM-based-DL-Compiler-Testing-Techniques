import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
   
        self.linear = torch.nn.Linear(32,64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 1
        v3 = v2 + 1
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 16, 16)
