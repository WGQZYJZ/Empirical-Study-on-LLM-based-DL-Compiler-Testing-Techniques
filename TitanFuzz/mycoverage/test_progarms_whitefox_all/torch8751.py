import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        v0 = x1
        v0[torch.tensor([0]), 0]
        return v0
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3)
