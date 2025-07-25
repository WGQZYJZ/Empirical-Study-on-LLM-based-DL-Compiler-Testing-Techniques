import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
        self.linear2 = torch.nn.Linear(10, 20)
        self.linear3 = torch.nn.Linear(20, 30)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.tanh(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3)

# Apply forward propagation
