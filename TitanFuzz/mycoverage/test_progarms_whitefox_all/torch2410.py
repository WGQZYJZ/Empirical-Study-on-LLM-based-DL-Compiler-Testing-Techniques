import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.nn.functional.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs (inputs2 is used so as to avoid in-place operations)
x1 = torch.randn(10)
x2 = x1.clone()
