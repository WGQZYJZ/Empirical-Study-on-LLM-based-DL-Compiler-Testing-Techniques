import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:x1.size(2)]
        v4 = torch.cat([v1, v3], dim=1)
        return v4.size(0)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model with different sizes
x1 = torch.randn(1, 5, 64, 64)
x2 = torch.randn(1, 5, 65, 64)
x3 = torch.randn(1, 5, 64, 32)
