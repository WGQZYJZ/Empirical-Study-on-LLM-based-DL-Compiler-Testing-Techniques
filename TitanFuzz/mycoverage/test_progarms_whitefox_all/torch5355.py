import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v = [torch.mm(x1, x2) for _ in range(2)] + list(range(5))
        return torch.cat(v, 0)
m = Model()
# Inputs to the model
x1 = torch.randn(4, 4)
x2 = torch.randn(4, 4)
