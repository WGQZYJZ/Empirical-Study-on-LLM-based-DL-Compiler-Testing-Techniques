import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(12, 8)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 * torch.clamp(v1 + 3, 0, 6)
        v3 = v2 / 6
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 12)
