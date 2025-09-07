import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.pool2d = torch.nn.MaxPool2d((2,2))
    def forward(self, x):
        x_b = self.pool2d(x)
        x_a = x - x_b
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 8, 8)
