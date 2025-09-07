import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 3)
        self.fc2 = torch.nn.Linear(3, 7)
 
    def forward(self, x):
        out = self.fc1(x)
        out = self.fc2(out)
        return torch.nn.functional.relu(out, inplace=True) - 35.0

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
