import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(250, 250)
 
    def forward(self, x):
        y = self.linear(x)
        y1 = torch.relu(y)
        return y1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 250)
