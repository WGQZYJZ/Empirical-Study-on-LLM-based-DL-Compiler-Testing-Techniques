import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.nn.functional.dropout(x, training=True)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 2, 2)
