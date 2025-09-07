import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        return F.dropout(x, p=0.5)
m = Model()
# Inputs to the model
x = torch.randn(1, 2, 2)
