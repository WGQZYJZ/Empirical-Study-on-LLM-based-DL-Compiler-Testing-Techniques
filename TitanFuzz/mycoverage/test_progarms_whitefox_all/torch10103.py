import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1):
        v1 = torch.nn.functional.selu(x1, alpha=0.5, scale=1.5)
        return v1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
