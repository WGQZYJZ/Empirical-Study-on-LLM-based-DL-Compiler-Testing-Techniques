import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 1, 3, 2)
        v3 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)
        return v1, v2, v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 1, 2, device='cpu')
x2 = torch.randn(1, 2, 1, 2, device='cpu')
