import torch
from torch import nn

class Model2(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.tanh(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
