import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x4, x4)  # noqa: F841
        v2 = torch.mm(x3, x3)  # noqa: F841
        v3 = torch.mm(x1, x1)  # noqa: F841
        v4 = x1 + x2 + x3  # noqa: F841
        v5 = torch.mm(x1, x1)  # noqa: F841
        return v1 + v2 + v3
m = Model()
# Inputs to the model
x1 = torch.randn(5, 5)
x2 = torch.randn(5, 5)
x3 = torch.randn(5, 5)
x4 = torch.randn(5, 5)
