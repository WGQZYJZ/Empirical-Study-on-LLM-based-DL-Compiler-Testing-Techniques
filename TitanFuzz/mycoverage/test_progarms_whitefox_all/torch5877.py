import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 1
        v8 = torch.nn.functional.relu(v2)
        return v8

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 256)
