import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5)
        b1 = F.dropout(x1, p=0.5)
        x2 = torch.nn.functional.dropout(x1, p=0.5)
        x3 = F.dropout(x1, p=0.5)
        return x2 * x3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
