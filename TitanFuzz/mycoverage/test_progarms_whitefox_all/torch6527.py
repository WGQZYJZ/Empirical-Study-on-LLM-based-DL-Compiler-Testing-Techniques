import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(3, 4)
    def forward(self, x3):
        v1 = torch.nn.functional.linear(x3, self.linear1.weight, self.linear1.bias)
        v2 = v1.permute(0, 2, 1)
        v3 = torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias)
        v4 = v2.permute(0, 2, 1)
        return v1
m = Model()
# Inputs to the model
x3 = torch.randn(1, 2, 2)
