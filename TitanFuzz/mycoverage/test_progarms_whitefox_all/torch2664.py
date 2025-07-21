import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 3)
    def forward(self, x):
        x = self.layers(x)
        x = torch.cat((x, x), dim=2)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
