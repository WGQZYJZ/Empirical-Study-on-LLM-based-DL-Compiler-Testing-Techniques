import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 10)
        self.bn = torch.nn.BatchNorm2d(1024)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.bn(v1)
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1024, 1, 1)
