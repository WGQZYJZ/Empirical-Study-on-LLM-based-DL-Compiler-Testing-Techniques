import torch
from torch import nn

class ModelTanh(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(259, 128, (6, 1), stride=(48, 1), bias=True)
    def forward(self, x):
        v1 = torch.tanh(self.conv2d(x))
        return v1
m = Model()
# Inputs to the model
x = torch.randn(1, 259, 20, 2)
