import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2)
        v3 = torch.bmm(v1, x2.permute(0, 2, 1))
        v4 = torch.matmul(v2, v1)
        v5 = v4.permute(0, 2, 1)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
