import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
    def forward(self, x1):
        v1 = self.linear(...,...,...,...)
        v2 = v1.permute(...)
        v3 = torch.max(...,..., dim=-1)[0]
        x2 =...
        return x1 - x2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 1)
