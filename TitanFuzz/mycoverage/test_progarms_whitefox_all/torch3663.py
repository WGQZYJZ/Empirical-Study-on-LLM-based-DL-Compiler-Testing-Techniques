import torch
from torch import nn

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = v1 - 1
        v3 = F.relu(v2)
        return v3

m = Model()
# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 3)
