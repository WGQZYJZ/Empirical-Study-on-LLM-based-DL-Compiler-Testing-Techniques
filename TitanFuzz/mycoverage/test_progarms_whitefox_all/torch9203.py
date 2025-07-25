import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.size = size
 
    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:self.size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

m = Model()
# Initializing the model
m = Model(size=5)

# Inputs to model
x1 = torch.randn(1, 40, 64, 64)
x2 = torch.randn(1, 30, 64, 64)
x3 = torch.randn(1, 20, 64, 64)
