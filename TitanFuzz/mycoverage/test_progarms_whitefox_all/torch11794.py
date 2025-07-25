import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, 5, stride=2)
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.conv2 = torch.nn.Conv2d(3, 8, 3, stride=2)
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = F.relu(v1)
        v3 = self.bn1(v2)
        v4 = self.conv2(v3)
        return v4
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 32, 32)
