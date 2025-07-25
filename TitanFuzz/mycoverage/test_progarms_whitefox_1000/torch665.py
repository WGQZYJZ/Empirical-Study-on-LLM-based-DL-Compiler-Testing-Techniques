import torch
from torch import nn


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 2)
    def forward(self, x):
        x = x + torch.rand(2, 2)
        x = self.layers(x)
        x = torch.stack((x, x, x), dim=1)
        x = x.flatten(start_dim=2)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
