import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        return torch.cat(torch.cat(torch.cat(x1, x2, 0), x1, 0), x2, 0)
m = Model()
# Inputs to the model
x1 = torch.randn(512, 2)
x2 = torch.randn(128, 2)
