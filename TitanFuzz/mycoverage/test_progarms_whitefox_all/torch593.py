import torch
from torch import nn

import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1,1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1)
