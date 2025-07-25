import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.rand(v1.shape)
        v3 = v1 + v2
        return torch.relu(v3)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
