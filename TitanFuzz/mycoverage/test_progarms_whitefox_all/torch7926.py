import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        x2 = F.dropout(x1, p=0.5)
        return x2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
