import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model(32, 64)

# Input to the model
x1 = torch.randn(1, 32)
