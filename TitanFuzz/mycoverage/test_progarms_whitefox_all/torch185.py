import torch
from torch import nn

class Model(torch.nn.Module):
m = Model()
def __init__(self):
    super().__init__()
    self.linear = torch.nn.Linear(93, 1)

def forward(self, x1):
    v1 = self.linear(x1)
    v2 = torch.sigmoid(v1)
    return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 93)
