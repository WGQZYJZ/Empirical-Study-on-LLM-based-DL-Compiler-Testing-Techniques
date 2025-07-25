import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 4, 1, stride=-1, padding=0)
        self.conv2 = torch.nn.Conv2d(2, 4, 1, stride=-1, padding=0)
    def forward(self, x, y):
        v1 = self.conv1(x)
        v2 = self.conv2(y)
        v3 = v1 + v2
        return v3
m = Model()
# Inputs to the model
x = torch.randn(1, 2, 32, 32)
y = torch.randn(1, 2, 32, 32)
