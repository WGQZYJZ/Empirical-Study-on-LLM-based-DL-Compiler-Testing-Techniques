import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(64, 64, 1, stride=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(2, 64, 10, 10)
