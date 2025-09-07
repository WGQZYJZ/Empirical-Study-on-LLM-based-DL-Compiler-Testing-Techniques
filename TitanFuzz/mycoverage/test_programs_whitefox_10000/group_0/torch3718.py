import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(196, 196)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.fc(x)
        v2 = self.relu(v1)
        v3 = v1 * v2
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(6, 196)
