import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10, False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = torch.sigmoid(v1)
        v6 = v1 * v3
        return v6

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
