import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 8)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = F.relu(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
