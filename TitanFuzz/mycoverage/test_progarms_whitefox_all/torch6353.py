import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inp1 = torch.randn(3, 3)
        self.inp2 = torch.randn(3, 3)
    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = torch.mm(x1, x1)
        v3 = v1 + self.inp2
        v4 = torch.mm(x1, x1)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3)
