import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v1 = torch.nn.functional.linear(x2, torch.ones([1, 2048], dtype=torch.float32))
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 2048)
