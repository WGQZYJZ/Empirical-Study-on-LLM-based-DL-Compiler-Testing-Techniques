import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x, y):
        v1 = torch.cat([x, y], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, :x.shape[2]]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 10, 20)
x2 = torch.randn(1, 10, 20)
