import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.squeeze(v1)
        v2 = v2 + 1.5
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3)
x2 = torch.randn(3, 3)
