import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v3 = x2 + v1
        v6 = torch.relu(v3)
        v7 = self.conv2(v6)
        v8 = x2 + v7
        v9 = torch.relu(v8)
        v11 = self.conv3(v9)
        v15 = x1 + v11
        v19 = torch.relu(v15)
        return v19
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 16, 64, 64)
