import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.rand(1, 1024)
