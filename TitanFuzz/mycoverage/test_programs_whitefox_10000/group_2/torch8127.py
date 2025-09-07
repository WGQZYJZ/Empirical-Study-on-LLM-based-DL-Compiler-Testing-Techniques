import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
    def forward(self, x1):
        return torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
m = Model()
# Inputs to the model
x1 = torch.randn(2, 2, 2)
