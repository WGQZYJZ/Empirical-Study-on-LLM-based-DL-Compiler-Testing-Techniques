import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        z = x * torch.tensor([[[[1.0]]]])
        return z
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 32, 64)
