import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 48)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.nn.functional.relu(v1)
        return v2
    
m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 32)
x = torch.reshape(x, (1, 32, 1, 1))
