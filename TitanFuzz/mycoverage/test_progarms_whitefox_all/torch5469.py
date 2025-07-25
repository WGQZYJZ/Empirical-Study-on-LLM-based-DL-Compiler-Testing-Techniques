import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(4, 2)
        self.stack = torch.stack
    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x, x, x), dim=0)
        return x.sum(dim=0)
m = Model()
# Inputs to the model
x = torch.randn(2, 4)
