import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4, x5):
        v1 = torch.cat([x1, x2, x3, x4, x5], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:384]
        v4 = torch.cat([x1, v3], dim=1)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 23, 56, 56)
x2 = torch.randn(1, 9223372036854775807, 40, 40)
x3 = torch.randn(1, 131072, 32, 32)
x4 = torch.randn(1, 262144, 24, 24)
x5 = torch.randn(1, 384, 16, 16)
