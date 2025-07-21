import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x2):
        v4 = self.linear(x2)
        v5 = torch.sigmoid(v4)
        v1 = v4 * v5
        return v1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 3)
