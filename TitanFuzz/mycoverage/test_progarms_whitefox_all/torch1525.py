import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2, bias=False)
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, bias=None)
        a1 = v1.permute(0, 2, 1)
        v2 = torch.nn.functional.relu(a1)
        return (v1, v2)
m = Model()
# Inputs to the model
x1 = torch.randn(3, 2, 2)
