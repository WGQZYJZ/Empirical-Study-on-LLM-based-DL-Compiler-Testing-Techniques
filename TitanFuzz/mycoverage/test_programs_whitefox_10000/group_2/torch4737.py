import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = Linear(16, 8)
 
    def forward(self, x):
        v1 = self.linear(x)
        return torch.sigmoid(v1)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 16)
