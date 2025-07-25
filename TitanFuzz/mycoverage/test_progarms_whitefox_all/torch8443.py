import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu6 = torch.nn.ReLU6()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.norm = torch.nn.BatchNorm2d(8,'sync')
        self.flatten = torch.nn.Flatten(start_dim=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.norm(v1)
        v3 = self.relu6(v2)
        v4 = self.flatten(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
