import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x0):
        v0 = x0
        v1 = torch.nn.functional.linear(v0, self.linear.weight, self.linear.bias)
        return v1.permute(0, 2, 1)
m = Model()
# Inputs to the model
x0 = torch.randn(1, 2, 2)
