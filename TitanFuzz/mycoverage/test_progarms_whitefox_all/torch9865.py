import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(7, 2)
       
    def forward(self, x1):
        return self.linear(x1)

m = Model()
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 7)
