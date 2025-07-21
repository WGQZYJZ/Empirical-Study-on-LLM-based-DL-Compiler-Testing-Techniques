import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(4, 1)
    def forward(self, x):
        x = self.layers(x)
        y = torch.cat((x, x), dim=0)
        x = torch.flatten(x, start_dim=0)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 4)
