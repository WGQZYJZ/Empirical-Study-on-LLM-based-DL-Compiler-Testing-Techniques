import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(6, 10)
 
    def forward(self, input):
        x = self.linear(input)
        x = torch.relu(x)
        return x

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
input = torch.randn(1, 6)
