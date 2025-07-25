import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v0 = x1.permute(0, 2, 1)
        v1 = x1.permute(0, 2, 1)
        v2 = v0.permute(0, 2, 1)
        v3 = v1.permute(0, 2, 1)
        v4 = x1.permute(0, 2, 1)
        v5 = x1.permute(0, 2, 1)
        v6 = torch.bmm(v4, x2)
        return torch.matmul(v6, v5)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
