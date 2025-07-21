import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = torch.nn.Linear(100, 50)

    def forward(self, x):
        x1 = self.linear_layer(x)
        y = x1 - 50
        return y

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 100)
