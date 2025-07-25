import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 100)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.nn.functional.gelu(v1)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 100)
