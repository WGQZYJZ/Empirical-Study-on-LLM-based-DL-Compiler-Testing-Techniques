import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(6,12)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = l1 * torch.clamp(torch.clamp(-3.0 + l1, min=0), max=6)
        l3 = l2 / 6
        return l3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 6)
