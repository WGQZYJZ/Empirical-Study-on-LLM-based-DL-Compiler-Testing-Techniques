import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 64, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        return v3 * 6

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16)
