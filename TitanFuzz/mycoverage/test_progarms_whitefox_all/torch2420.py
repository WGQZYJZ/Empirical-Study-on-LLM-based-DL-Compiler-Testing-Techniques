import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 4)
    def forward(self, x):
        x = self.layers(x)
        x = torch.cat((x, x), dim=0)
        return x
m = Model()
# Inputs to the model
x = torch.randn(4, 2)
