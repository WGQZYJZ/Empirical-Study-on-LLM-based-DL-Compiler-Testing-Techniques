import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers_1 = nn.Linear(2, 2)
        self.layers_2 = nn.Linear(2, 2)
    def forward(self, x):
        x = self.layers_1(x)
        x = self.layers_2(x)
        x = torch.stack((x, x, x), dim=1)
        x = torch.flatten(x, start_dim=1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
