import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.affine = torch.nn.Linear(8, 16)
 
    def forward(self, x1, x2):
        v1 = self.affine(x1)
        v2 = v1 + x2
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8)
x2 = torch.randn(2, 16)
