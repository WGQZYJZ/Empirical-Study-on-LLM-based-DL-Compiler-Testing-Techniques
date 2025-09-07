import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.linear = torch.nn.Linear(input_size, input_size)
 
    def forward(self, x):
        v = self.linear(x)
        v = torch.nn.functional.relu(v)
        return v

m = Model()
# Initializing the model
m = Model(10)

# Inputs to the model
x1 = torch.randn(1, 10)
