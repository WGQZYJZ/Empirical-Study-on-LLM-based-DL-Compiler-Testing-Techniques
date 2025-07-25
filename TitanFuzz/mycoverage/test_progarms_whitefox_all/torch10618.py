import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.25
        v3 = torch.relu(v2)
        return v1, v2, v3
 
m = Model()
# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(1, 4)
