import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1).contiguous()
        v3 = torch.bmm(v2, v1)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(3, 2, 2)
x2 = torch.randn(3, 2, 2)
