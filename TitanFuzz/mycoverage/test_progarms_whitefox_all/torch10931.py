import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1204368, 130)
    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = v2.permute(0, 2, 1)
        x2 = v2.permute(0, 2, 1)
        v3 = torch.matmul(x2, v3)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1204368, 1)
