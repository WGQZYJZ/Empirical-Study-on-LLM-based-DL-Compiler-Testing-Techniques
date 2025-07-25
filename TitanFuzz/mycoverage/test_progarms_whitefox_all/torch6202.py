import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(20, 10)
    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x, x, x), dim=1)
        x = x.flatten(start_dim=1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 20)
