import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(33, 33, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(33, 8, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(16, 4, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        v8 = torch.relu(v7)
        return v8
m = Model()
# Inputs to the model
x1 = torch.randn(1, 33, 256, 256)
