import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5)
        return t1.mul(2) ** 2
m = Model()
# Inputs to the model
x1 = torch.randn(4,)
