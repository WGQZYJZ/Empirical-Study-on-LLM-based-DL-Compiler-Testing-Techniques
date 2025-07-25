import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x1, x2, x3):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = v2 + x3
        v4 = F.relu(v3)
        return v4

m = Model()
# Initializing the first module
l = torch.nn.Linear(10, 20)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 10)
x2 = torch.randn(2, 20)
x3 = torch.randn(2, 20)
