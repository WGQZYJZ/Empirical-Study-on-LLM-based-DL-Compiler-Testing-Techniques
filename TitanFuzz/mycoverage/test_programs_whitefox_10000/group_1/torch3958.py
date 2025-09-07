import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
 
    def forward(self, x):
        linear = self.linear(x)
        tanh = torch.tanh(linear)
        return tanh

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 16)
