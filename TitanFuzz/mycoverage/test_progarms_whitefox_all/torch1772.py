import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
torch.manual_seed(0)
x1 = torch.randn(1, 3, 64, 64)
