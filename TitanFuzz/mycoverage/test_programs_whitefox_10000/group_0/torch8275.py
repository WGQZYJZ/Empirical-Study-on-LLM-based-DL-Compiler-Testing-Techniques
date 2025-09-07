import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 2)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        x = self.linear(x1)
        x2 = self.relu(x)
        return x2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 100)
