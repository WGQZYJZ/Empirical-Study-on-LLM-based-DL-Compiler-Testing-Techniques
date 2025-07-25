import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear( 100, 3000)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - torch.ones(v1.size())
        return v2


m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1000, 100)  # Input values
