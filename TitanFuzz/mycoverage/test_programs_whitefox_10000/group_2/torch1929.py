import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()
    def forward(self, x):
        x = torch.cat([x, x], dim=1)
        return self.relu(x)
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
