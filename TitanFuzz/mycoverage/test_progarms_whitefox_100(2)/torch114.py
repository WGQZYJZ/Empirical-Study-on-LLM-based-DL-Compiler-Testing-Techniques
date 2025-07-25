import torch
from torch import nn

class Model(torch.nn.Module):
    
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(5, 5)
        self.fc2 = torch.nn.Linear(5, 5)
    
    def forward(self, x1, x2, other):
        v1 = self.fc1(x1)
        v2 = self.fc2(x2)
        v3 = v1 + v2 + other
        return v3

m = Model()
# Initializing the model 
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5)
x2 = torch.randn(1, 5)
other = torch.randn(1, 5)
