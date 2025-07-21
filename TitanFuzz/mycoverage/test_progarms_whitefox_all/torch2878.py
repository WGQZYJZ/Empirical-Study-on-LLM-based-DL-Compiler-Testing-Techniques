import torch
from torch import nn

class ModelTanh(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 40, 1, stride=1)
        self.tanh = torch.nn.Tanh()
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        return v2
m = Model()
# Inputs to the model
x = torch.randn(1, 16, 100, 100)
