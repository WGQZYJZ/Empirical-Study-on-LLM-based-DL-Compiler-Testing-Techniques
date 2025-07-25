import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)
    def forward(self, x1):
        y = self.linear1(x1)
        y = y.permute(0,2,1)
        v3 = torch.nn.functional.linear(y, self.linear2.weight, self.linear2.bias)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
