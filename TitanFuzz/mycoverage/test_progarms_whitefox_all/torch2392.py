import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        v1 = torch.sigmoid(torch.nn.Softplus(self.linear(x1)))
        return torch.cos(v1)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
