import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v3 = torch.relu(v1)
        v4 = v3 * x1
        v5 = torch.relu(v4)
        v6 = v3 + v5
        v7 = torch.relu(v6)
        v8 = self.conv2(v7)
        v11 = v8 + x2
        v12 = torch.relu(v11)
        v13 = self.conv3(v12)
        v15 = v13 + x3
        v16 = torch.relu(v15)
        return v16
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 16, 64, 64)
x3 = torch.randn(1, 16, 64, 64)
