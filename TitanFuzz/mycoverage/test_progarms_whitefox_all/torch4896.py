import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = x1.permute(2, 0, 1)
        v2 = torch.bmm(v1, x2)
        v3 = v1.permute(0, 2, 1)
        return torch.bmm(v3, v2)
m = Model()
# Inputs to the model
x1 = torch.randn(2, 1, 2)
x2 = torch.randn(2, 1, 2)
