import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model (passing a specific tensor `other`)
m = Model(torch.randn(5))

# Inputs to the model
x1 = torch.randn(1, 3)
