import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=2, groups=2)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=1, groups=2)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3, groups=2)
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.relu(v2)
        v4 = v3 + self.conv3(x2)
        v5 = torch.relu(v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 16, 64, 64)
