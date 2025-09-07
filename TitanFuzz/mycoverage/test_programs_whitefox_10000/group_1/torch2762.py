import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(10, 1)
 
    def forward(self, x):
        v5 = torch.sigmoid(self.lin(x))
        return v5

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 10)
