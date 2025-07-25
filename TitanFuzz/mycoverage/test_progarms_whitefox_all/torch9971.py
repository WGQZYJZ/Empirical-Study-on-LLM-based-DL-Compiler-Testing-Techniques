import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(4, 4, 3, stride=1, padding=1, dilation=0, groups=1)
        self.conv2 = torch.nn.Conv2d(4, 4, 3, stride=1, padding=1, dilation=0, groups=1)
        self.conv3 = torch.nn.Conv2d(4, 4, 3, stride=1, padding=1, dilation=0, groups=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv1(x1)
        v3 = v1 + v2
        v4 = torch.relu(v3)
        v5 = self.conv1(x1)
        v6 = self.conv2(x1)
        v7 = v5 + v6
        v8 = torch.relu(v7)
        v9 = self.conv2(x1)
        v10 = self.conv3(x1)
        v11 = v9 + v10
        v12 = torch.relu(v11)
        v13 = v4 + v8 + v12
        return v13
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
