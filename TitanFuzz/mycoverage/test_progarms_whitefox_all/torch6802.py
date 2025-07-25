import torch
from torch import nn

x2 = torch.randn(1, 12)
other = torch.tensor([[2.8, 3.4, 2.5, 2.6, 2.5]])
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(12, 16, False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 12)
