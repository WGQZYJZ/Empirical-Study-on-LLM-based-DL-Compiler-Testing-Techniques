import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.param = torch.randn(1, 2, 3, requires_grad=True)
    def forward(self, x1):
        x2 = torch.rand_like(x1) + self.param
        x3 = F.dropout(x1, p=0.5)
        x4 = x2 + x3
        return x4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
