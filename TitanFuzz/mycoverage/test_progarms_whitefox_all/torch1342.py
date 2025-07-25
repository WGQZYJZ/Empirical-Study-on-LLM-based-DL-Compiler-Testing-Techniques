import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 16)
        self.relu1 = torch.nn.ReLU6()
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64)
