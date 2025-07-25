import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.7)
    def forward(self, x1):
        x2 = self.dropout(x1)
        x3 = torch.rand_like(x1)
        return x3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
