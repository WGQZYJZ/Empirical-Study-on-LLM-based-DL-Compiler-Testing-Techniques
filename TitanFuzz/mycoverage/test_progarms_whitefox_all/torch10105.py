import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 8)
        self.layers_2 = nn.Linear(2, 8)
    def forward(self, x):
        x = self.layers_2(x)
        x = self.layers(x)
        x = torch.stack((x, x), dim=1)
        x = x[1:10, ::]
        x = torch.flatten(x, start_dim=1)
        x = x[0]
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
