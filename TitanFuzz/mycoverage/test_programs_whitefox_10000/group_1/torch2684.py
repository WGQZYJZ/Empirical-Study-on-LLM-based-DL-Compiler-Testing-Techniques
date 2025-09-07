import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8, bias=True)
 
    def forward(self, x1):
        t1 = self.linear(x1)
        v1 = torch.tanh(t1)
        return v1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1)
