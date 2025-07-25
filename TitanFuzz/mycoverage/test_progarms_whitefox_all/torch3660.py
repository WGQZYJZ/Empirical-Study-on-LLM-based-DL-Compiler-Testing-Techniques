import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
        self.relu6 = torch.nn.ReLU6(inplace=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v4 / 6
        return v5

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.ones(1, 16)
