import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        x1_plus1 = torch.add(x1, 1)
        v = torch.nn.functional.linear(x1_plus1, self.linear.weight, self.linear.bias)
        return v
m = Model()
# Inputs to the model
x1 = torch.randn((1, 1, 2))
