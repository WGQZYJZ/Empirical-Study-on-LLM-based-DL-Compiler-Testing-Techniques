import torch
from torch import nn

class Model(nn.Module):
    __init__(self):
        super().__init__()
        self.Linear = torch.nn.Linear(8, 8)
 
    def forward(self, x1):
        v1 = self.Linear(x1)
        v2 = torch.tanh(v1)
        return v2


m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
