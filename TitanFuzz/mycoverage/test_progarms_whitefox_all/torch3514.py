import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 63)
 
    def forward(self, x1, other=1.3):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v1, v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 128)
