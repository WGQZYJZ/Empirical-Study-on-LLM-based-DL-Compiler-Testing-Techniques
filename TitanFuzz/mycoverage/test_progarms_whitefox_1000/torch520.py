import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = x.view(-1)
        z = y.narrow(0, 0, 2).squeeze(0).unsqueeze(0)
        x = z[0]
        y = x.add(-1)
        return y
m = Model()
# Inputs to the model
x = torch.randn(5, 5)
