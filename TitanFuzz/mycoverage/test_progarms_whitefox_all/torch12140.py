import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.rmatmul(self.linear.weight)
        return v2.rmatmul(self.linear.weight)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
