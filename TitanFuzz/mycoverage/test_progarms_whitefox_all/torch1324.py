import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = (v1 * v1 * v1) * 0.044715
        v4 = v3 + v2
        v7 = 0.7978845608028654
        v5 = v4 * v7
        v6 = torch.tanh(v5)
        v8 = 1
        v9 = v6 + v8
        v10 = v2 * v9
        return v10

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
