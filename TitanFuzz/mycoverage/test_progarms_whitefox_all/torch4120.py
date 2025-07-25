import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(4, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 1, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv2(v3)
        v5 = F.sigmoid(v4)
        v6 = v4 * v5
        v7 = self.conv3(v6)
        v8 = torch.sigmoid(v7)
        v9 = v7 * v8
        return v1, v2, v3, v4, v5, v6, v8, v9
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
