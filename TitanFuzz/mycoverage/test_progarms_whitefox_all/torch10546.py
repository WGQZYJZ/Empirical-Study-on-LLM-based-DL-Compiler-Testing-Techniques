import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:x1.size(2)]
        v4 = torch.cat((v1, v3), dim=1)
        return v4

m = Model()
# Initializing the model
m1 = Model()

# Inputs to the model
x = torch.randn(1, 230400, 64, 64)
y = torch.randn(1, 153600, 64, 64)
