import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        x2 = torch.rand_like(x1)
        x3 = F.dropout(x1, p=0.5, training=False)
        x4 = x3 + x2
        return x3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
