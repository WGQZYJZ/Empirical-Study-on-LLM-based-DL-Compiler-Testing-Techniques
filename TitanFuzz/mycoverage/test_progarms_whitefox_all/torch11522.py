import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1):
        v1 = torch.cat([x1], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0::1000]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
