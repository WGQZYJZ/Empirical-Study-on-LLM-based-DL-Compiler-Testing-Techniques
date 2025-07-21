import torch
from torch import nn

import torch.nn as nn

class Model(nn.Module):
    def __init__():
        super().__init__()
        self.linear = nn.Linear(20, 20)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - 1
        v3 = self.relu(v2)
        return v3
 
m = Model()
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 20)
