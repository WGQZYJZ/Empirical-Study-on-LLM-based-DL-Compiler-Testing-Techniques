import torch
from torch import nn

class ModelTanh(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x):
        x = self.conv(x)
        x = torch.tanh(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
