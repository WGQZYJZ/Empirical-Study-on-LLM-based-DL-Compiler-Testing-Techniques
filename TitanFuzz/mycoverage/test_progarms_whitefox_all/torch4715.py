import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v1 = self.conv2(v1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 8, 8)
