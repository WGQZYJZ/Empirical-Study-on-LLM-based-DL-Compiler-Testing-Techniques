import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 16)
        self.linear2 = torch.nn.Linear(16, 8)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.linear2(v3)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
