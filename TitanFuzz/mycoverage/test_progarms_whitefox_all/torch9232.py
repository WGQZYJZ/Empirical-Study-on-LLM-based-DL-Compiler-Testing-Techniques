import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1, groups=8)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1, groups=8)
    def forward(self, x1):
        v1 = F.relu6(self.conv1(x1))
        v2 = F.relu6(self.conv2(x1))
        v3 = v1 + v2
        v4 = self.bn1(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
