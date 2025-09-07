import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        y = self.linear(x)
        z = y + 1.1
        k = torch.nn.ReLU(inplace=True)(z)
        return k

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3)
