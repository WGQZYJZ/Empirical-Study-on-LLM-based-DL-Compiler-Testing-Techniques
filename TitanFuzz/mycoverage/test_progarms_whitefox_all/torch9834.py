import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 8)
    def forward(self, x1):
        v1 = torch.transpose(x1, 1, 2)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 128, 2)
