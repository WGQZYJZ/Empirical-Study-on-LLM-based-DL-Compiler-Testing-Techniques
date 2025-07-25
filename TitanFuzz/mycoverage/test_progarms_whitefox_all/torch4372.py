import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(1, 1)
    def forward(self, x):
        x = self.layers(x)
        x = torch.stack([x], dim=1)
        x = torch.squeeze(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 1)
