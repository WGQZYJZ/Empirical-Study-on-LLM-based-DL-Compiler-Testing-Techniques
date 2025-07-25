import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v = x1 + torch.mm(x1, x2)
        return v.squeeze(0)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 3)
x2 = torch.randn(3, 3)
