import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linera(32,32)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = l1 * torch.clamp(l1+3,0,6)
        l3 = l2 / 6

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.rand(1, 32)
