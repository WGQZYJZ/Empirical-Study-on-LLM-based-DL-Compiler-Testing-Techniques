import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 10, 8)
