import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.flatten = torch.nn.Flatten(start_dim=1)
        self.linear = torch.nn.Linear(51*51*8, 10)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.flatten(v1)
        v3 = self.linear(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
