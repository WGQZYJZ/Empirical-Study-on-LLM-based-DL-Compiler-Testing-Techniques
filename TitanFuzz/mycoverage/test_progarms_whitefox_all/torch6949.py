import torch
from torch import nn

class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = F.dropout(x, p=0.2, training=False)
        x = torch.rand_like(x)
        return x
# Inputs to the model
x1 = torch.randn(2, 3)
