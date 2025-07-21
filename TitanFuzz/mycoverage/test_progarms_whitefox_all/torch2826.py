import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        x2 = self.linear(x1)
        x3 = torch.relu(x2)
        return x3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3)
