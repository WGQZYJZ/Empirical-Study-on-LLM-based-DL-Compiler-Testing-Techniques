import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, p):
       return torch.nn.functional.dropout(p + 0.5, inplace=False)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 10, 2, 2)
