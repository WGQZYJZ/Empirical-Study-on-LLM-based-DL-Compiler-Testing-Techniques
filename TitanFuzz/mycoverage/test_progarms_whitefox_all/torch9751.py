import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = v1 + other_tensor
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
other_tensor = torch.randn(1, 32)
x2 = torch.randn(4, 16)
