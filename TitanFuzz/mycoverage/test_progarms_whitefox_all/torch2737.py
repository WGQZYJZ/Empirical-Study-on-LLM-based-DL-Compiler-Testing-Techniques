import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2))
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:32532]
        v4 = torch.cat((v1, v3), 1)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32650, 112, 112)
x2 = torch.randn(1, 191350, 112, 112)
