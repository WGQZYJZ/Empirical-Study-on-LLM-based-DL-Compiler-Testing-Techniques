import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        y = torch.randn(1, 2, 2)
        x2 = torch.full_like(v2, 2.)
        z = x2 + y
        return self.linear(v1)
m = Model()
# Inputs to the model
x1 = torch.randn(5, 3, 2)
