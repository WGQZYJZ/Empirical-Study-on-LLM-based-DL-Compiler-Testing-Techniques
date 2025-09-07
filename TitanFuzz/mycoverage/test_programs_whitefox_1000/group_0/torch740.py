import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(3, 2)
    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x), dim=0)
        x = torch.flatten(x, start_dim=0)
        return x
m = Model()
# Inputs to the model
x = torch.randn(3, 3)
