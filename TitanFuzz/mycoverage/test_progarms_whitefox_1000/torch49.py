import torch
from torch import nn

 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.4
        v3 = torch.tanh(v2)
        return v3

m = Model()
# Initializing the model
m2 = Model()

# Inputs to the model
x1 = torch.randn(1, 32)
