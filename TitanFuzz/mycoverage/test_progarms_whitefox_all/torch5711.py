import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 10)
 
    def forward(self, x):
        x = self.linear(x)
        y = x * torch.clamp(x + 3, min=0, max=6) / 6
        return y

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1)
