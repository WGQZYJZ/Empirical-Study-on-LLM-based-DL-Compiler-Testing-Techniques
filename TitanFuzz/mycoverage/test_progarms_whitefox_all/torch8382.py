import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(16, 32)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16)
