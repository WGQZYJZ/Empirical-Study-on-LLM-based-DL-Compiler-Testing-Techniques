import torch
from torch import nn

class ModelTanh(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(torch.tanh(torch.tanh(v1)))
        return v2
m = Model()
# Inputs to the model
x = torch.randn(23, 3, 239, 239)
