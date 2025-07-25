import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(88, 116)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.relu(v1)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 88)
v2 = torch.randn(1, 116)
