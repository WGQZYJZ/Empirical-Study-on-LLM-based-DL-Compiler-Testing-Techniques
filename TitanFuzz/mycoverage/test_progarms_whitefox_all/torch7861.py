import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:20]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
y1 = torch.randn(1, 4, 6, 7)
y2 = torch.randn(1, 1, 5, 12)
y3 = torch.randn(1, 40, 2, 6)
