import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 512)
        self.other_linear = torch.nn.Linear(256, 512)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + self.other_linear(x)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 256)
