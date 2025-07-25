import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.addmm = torch.nn.Linear(3, 3)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.addmm.weight, self.addmm.bias)
        v2 = torch.cat([v1], 1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
