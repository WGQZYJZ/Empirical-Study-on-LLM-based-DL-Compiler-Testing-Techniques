import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:4611686018427387903]
        v3 = v1[:, 0:2]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64)
x2 = torch.randn(3, 64)
x3 = torch.randn(3, 32)
x4 = torch.randn(3, 32)
