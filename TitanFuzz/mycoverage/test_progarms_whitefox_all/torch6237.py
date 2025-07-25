import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        v3 = torch.matmul(x1, v2)
        v4 = torch.matmul(v2, x1)
        v5 = v1.permute(0, 2, 1)
        v6 = v2.permute(0, 2, 1)
        v7 = torch.matmul(v1, v2)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
