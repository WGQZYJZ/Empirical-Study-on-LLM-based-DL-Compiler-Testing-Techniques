import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 - 3.8859
        v3 = F.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 32)
