import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super(M, self).__init__()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 1 # other=1
        v3 = torch.clamp(v2, -1, 1)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5)
