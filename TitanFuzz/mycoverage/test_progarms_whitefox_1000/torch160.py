import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 / x1.size(-1)
        v3 = v2 + x3
        v4 = torch.softmax(v3, dim=-1)
        v5 = torch.matmul(v4, x3)
        return v5

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 4, 512)
x2 = torch.randn(2, 512, 512)
x3 = torch.randn(2, 4, 512)
