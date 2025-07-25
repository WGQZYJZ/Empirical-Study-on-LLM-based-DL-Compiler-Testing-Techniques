import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = torch.pow(v1, 3)
        v3 = v2.permute(0, 2, 1)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(2, 2, 2)
