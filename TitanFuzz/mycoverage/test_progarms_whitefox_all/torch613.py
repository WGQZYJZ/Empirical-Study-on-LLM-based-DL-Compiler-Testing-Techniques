import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 - 1
        v3 = v1 - other
        v4 = torch.relu(v3)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
