import torch
from torch import nn

import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 5)
 
    def forward(self, x1):
        v2 = self.linear(x1)
        v3 = v2 * 0.5
        v4 = v2 + (v2 * v2 * v2) * 0.044715
        v5 = v4 * 0.7978845608028654
        v6 = torch.tanh(v5)
        v7 = v6 + 1
        v8 = v3 * v7
        return v8

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(25, 5)
