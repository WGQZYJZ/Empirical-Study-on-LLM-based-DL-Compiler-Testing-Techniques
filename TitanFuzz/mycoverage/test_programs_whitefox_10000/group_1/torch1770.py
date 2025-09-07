import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, num_hidden):
        super().__init__()
        self.linear = torch.nn.Linear(9, num_hidden)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 - 1

m = Model()
# Initializing the model
m = Model(8)

# Inputs to the model
x = torch.randn(8, 9)
