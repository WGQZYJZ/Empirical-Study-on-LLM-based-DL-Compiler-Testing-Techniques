import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)
 
    def forward(self, x1, x2=None):
        if x2 is None:
            x2 = torch.ones((1,))
        v1 = self.linear(x1)
        v2 = v1 + x2
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2)
