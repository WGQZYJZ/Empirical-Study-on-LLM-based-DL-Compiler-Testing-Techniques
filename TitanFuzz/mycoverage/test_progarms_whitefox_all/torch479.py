import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
    
    def forward(self, x2, x3):
        v1 = self.linear(x2)
        v2 = v1 + x3
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 3)
x3 = torch.arange(8).reshape(1, 8).float()
