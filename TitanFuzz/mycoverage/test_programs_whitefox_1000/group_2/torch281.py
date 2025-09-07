import torch
from torch import nn

class ModelTanh(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3, stride=1, padding=0)
    def forward(self, x):
        v1 = torch.tanh(self.conv(x))
        return v1
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 13, 13)
