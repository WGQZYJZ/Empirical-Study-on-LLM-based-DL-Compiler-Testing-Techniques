import torch
from torch import nn


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(40, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 40)
