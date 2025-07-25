import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
 
    def forward(self, x2):
        v5 = self.linear(x2)
        v6 = torch.tanh(v5)
        return v6

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 3)
