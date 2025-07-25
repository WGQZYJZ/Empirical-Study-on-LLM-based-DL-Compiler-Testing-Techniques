import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 2, stride=2, padding=0)
        self.conv1 = torch.nn.Conv2d(3, 6, 3, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 3, 5, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(3, 6, 5, stride=2, padding=2)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv1(v1)
        v3 = self.conv2(x1)
        v4 = self.conv3(v3)
        return v2, v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
