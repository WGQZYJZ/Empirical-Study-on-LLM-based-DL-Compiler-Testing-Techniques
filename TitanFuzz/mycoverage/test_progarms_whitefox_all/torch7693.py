import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 32, (3, 3))
        self.conv2 = torch.nn.Conv2d(32, 48, (3, 3), padding=1)
        self.conv3 = torch.nn.Conv2d(48, 64, (3, 3), padding=1)
        self.conv4 = torch.nn.Conv2d(64, 3, (3, 3), padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv3(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.conv4(v6)
        v8 = torch.sigmoid(v7)
        return v8
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 257, 129)
