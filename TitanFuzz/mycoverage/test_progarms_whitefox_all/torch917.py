import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)
 
    def forward(self, x2):
        v2 = self.linear(x2)
        v3 = torch.sigmoid(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 1)
