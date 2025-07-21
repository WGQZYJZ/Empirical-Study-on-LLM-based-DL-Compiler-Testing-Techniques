import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        a = torch.nn.functional.dropout(x1, p=0.0)
        return torch.nn.functional.dropout(torch.nn.functional.dropout(a))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2)
