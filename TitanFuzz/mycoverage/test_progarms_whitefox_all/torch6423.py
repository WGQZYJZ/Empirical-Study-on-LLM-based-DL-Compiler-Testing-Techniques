import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 96, 3, stride=2)
        self.conv2 = torch.nn.Conv2d(96, 96, 1, stride=1)
        self.conv3 = torch.nn.Conv2d(96, 96, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(96, 160, 3, stride=1, dilation=1)
        self.conv5 = torch.nn.Conv2d(160, 160, 1, stride=2)
        self.conv6 = torch.nn.Conv2d(160, 160, 3, stride=1)
        self.conv7 = torch.nn.Conv2d(160, 160, 3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = self.conv6(v5)
        v7 = self.conv7(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 512, 384)
