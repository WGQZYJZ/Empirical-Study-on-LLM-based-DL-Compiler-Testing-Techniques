import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        return x.view(2, -1, 2)
m = Model()
# Inputs to the model
x = torch.randn(1, 2, 3)
