import torch
from torch import nn

t = torch.ones(1, 28, 28)
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 128)
 
    def forward(self, x2):
        v = torch.flatten(x2, 1)
        v = self.linear(v)
        v = torch.sigmoid(v)
        return v

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = t
__output2__ = m(x2)

# Inputs to the model
x2 = t
