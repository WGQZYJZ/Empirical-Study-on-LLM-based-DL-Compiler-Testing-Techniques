import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 1)
 
    def forward(self, x):
        f = self.linear(x)
        result = torch.abs(f - 0.5)
        return result

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 128)
