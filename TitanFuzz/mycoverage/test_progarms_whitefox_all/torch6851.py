import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 20)
v = m(x1)

