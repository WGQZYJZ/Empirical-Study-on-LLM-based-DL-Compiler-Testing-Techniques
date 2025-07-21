import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(4, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.tanh(v1)
        return v2

m = Model()
# Initializing the model
m = Model()
# Input to the model
x = torch.randn(3, 4)
# Model output
