import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4, x5, x6):
        v1 = torch.cat([x1, x2, x3, x4, x5, x6], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:5]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 128, 32, 32)
x2 = torch.randn(1, 128, 32, 32)
x3 = torch.randn(1, 128, 32, 32)
x4 = torch.randn(1, 128, 32, 32)
x5 = torch.randn(1, 128, 32, 32)
x6 = torch.randn(1, 128, 32, 32)
