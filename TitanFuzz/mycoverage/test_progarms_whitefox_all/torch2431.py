import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2, 8)
        self.fc2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = v1 + torch.zeros_like(v1)
        v3 = self.fc2(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2)
x2 = torch.randn(1, 2)
