import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.cat([x, x, x], dim=1)
        x = torch.cat([x, x, x], dim=1)
        x = torch.cat([x, x, x], dim=-1)
        x = torch.cat([x, x, x], dim=-1)
        x = x.view(-1, 6, 2)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
