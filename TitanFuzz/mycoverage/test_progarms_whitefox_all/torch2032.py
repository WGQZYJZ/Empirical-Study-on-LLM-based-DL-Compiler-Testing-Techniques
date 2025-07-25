import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 20, 3, stride=2, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(20)
        self.conv2 = torch.nn.Conv2d(20, 32, 3, stride=1, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(32)
        self.conv3 = torch.nn.Conv2d(32, 48, 4, stride=2, padding=1)
        self.bn3 = torch.nn.BatchNorm2d(48)
        self.conv4 = torch.nn.Conv2d(48, 80, 3, stride=2, padding=0)
        self.bn4 = torch.nn.BatchNorm2d(80)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.bn1(v1)
        v3 = torch.relu(v2)
        v4 = self.conv2(v3)
        v5 = self.bn2(v4)
        v6 = torch.relu(v5)
        v7 = self.conv3(v6)
        v8 = self.bn3(v7)
        v9 = torch.relu(v8)
        v10 = self.conv4(v9)
        v11 = self.bn4(v10)
        v12 = torch.relu(v11)
        return v12
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 128)
