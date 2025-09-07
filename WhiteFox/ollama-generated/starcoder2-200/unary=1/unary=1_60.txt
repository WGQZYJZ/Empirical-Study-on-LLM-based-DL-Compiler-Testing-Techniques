

import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         return torch.randn(32)

m = Model()

# Inputs to the model 
x1 = torch.randn(4)
__output__  = m(x1)

