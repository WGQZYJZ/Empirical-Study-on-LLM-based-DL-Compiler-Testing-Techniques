import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 64, bias=True)
 
    def forward(self, __input__):
        v1 = self.linear(__input__)
        v2 = torch.sigmoid(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(1, 256)
