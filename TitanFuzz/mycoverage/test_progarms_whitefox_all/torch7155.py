import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 32, 7, stride=3, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 64, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 128, 3, stride=4, padding=0)
        self.conv4 = torch.nn.Conv2d(256, 1, 5, stride=2, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = v4.permute(0, 1, 3, 2)
        v8 = torch.cat([v6, v7], 1)
        v9 = v8.permute(0, 1, 3, 2)
        v10 = self.conv4(v9)
        v11 = torch.relu(v10)
        return v11
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 128, 128)
