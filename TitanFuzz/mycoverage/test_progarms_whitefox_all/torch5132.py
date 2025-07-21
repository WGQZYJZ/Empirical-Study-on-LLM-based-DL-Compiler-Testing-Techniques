import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        v1 = torch.sum(x1, [2, 3])
        v2 = torch.softmax(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 3, 3)
