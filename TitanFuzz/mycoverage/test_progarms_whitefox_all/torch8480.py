import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        v1 = torch.ops.aten.where(x1, x1, x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(2, 2)
