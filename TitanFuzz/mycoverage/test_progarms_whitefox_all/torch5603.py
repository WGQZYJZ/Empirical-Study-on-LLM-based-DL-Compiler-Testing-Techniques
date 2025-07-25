import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(12, 24, bias=False)
        self.other = torch.randn(24)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(12)
x2 = torch.randn(24)
