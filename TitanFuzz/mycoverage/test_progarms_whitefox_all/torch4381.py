import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x4):
        v1 = self.conv2(x4)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        return v3
m = Model()
# Inputs to the model
x4 = torch.randn(1, 16, 64, 64)
