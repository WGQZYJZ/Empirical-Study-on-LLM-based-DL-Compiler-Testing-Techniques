import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Conv2d(64, 64, 1, stride = 1)
 
    def forward(self, x2):
       v1 = self.linear(x2)
       v2 = torch.relu(v1)
       return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 64, 1, 1)
