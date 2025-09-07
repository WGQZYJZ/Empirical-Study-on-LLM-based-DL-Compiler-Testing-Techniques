import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
        self.other_tensor = other_tensor
 
    def forward(self, x2):
        v2 = self.linear(x2)
        v3 = v2 + self.other_tensor
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
