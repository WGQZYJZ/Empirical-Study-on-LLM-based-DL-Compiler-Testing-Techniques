import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.stack((x, x, x), dim=1)
        x = torch.flatten(x, 1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
