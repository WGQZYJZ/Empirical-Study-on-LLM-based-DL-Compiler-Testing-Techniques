import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1, x2, x3, x4, x5):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.conv3(x3)
        v4 = self.conv4(x4)
        v5 = self.conv5(x5)
        v6 = v1 + v2
        v7 = v3 + v4
        v8 = v1 + v5 
        v9 = v7 + v8
        v10 = v6 + v9
        return v10
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 8, 8)
x2 = torch.randn(1, 3, 8, 8)
x3 = torch.randn(1, 3, 8, 8)
x4 = torch.randn(1, 3, 8, 8)
x5 = torch.randn(1, 3, 8, 8)
