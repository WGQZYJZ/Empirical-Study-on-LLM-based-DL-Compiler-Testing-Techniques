import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x1):
        w = self.linear(x1)
        z = torch.tanh(w)
        return z

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 20)
