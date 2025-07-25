import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.autograd.Variable(torch.rand_like(v1))
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.rand(1, 4)
