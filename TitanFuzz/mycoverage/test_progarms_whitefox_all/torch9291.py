import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = x1.view((1, -1)).dot(w1)
        v2 = F.relu(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Initializing weights
torch.manual_seed(10)
w1 = torch.rand(3072, 8)

