import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 12, (23, 6), stride=1, padding=10)
        self.conv2 = torch.nn.Conv2d(3, 12, (23, 6), stride=1, padding=10)
        self.conv3 = torch.nn.Conv2d(3, 12, (23, 6), stride=1, padding=10)
        self.conv4 = torch.nn.Conv2d(3, 12, (17, 6), stride=1, padding=8)
        self.conv5 = torch.nn.Conv2d(3, 12, (11, 6), stride=1, padding=6)
        self.conv6 = torch.nn.Conv2d(3, 12, (11, 6), stride=1, padding=6)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(x1)
        v4 = self.conv4(x1)
        v5 = self.conv5(x1)
        v6 = self.conv6(x1)
        v7 = v1 + v2 + v3 + v4 + v5 + v6
        v8 = torch.relu(v7)
        return v8
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 32)
