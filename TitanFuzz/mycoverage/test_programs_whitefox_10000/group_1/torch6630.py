import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.relu(x.permute((0, 3, 2, 1)))
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 2, 3, 4)
