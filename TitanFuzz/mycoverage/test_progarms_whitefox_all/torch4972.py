import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(10, 10)
 
    def forward(self, x, other):
        v1 = self.fc(x)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 10)
other = torch.randn(4, 10)
