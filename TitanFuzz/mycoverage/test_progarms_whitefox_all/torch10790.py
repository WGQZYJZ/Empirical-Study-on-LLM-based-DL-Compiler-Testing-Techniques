import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4, size):
        v1 = torch.cat([x1, x2, x3, x4], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 48, 48)
x2 = torch.randn(1, 3, 24, 24)
x3 = torch.randn(1, 3, 12, 12)
x4 = torch.randn(1, 3, 6, 6)
size = torch.randint(32, 56, [1])
