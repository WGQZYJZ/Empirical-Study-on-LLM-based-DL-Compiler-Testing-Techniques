import torch
from torch import nn

import torch.nn.functional as F

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(240, 240)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = F.relu(v3, inplace=True)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 240)
