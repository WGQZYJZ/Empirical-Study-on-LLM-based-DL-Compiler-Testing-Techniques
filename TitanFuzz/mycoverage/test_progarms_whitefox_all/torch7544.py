import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 3)
        self.expand = torch.expand
        self.cat = torch.cat
    def forward(self, x):
        x = self.layers(x)
        x = self.expand(x, (2, 2, 3))
        x = self.cat([x, x])
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
