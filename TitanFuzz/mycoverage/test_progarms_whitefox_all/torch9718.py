import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(6, 12, 5, stride=2, padding=2)
        self.conv3 = torch.nn.Conv2d(12, 24, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(24, 12, 3, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(12, 48, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(48, 24, 3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        v8 = torch.relu(v7)
        v9 = self.conv5(v8)
        v10 = torch.relu(v9)
        v11 = self.conv6(v10)
        v12 = torch.relu(v11)
        return v12
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 768, 768)
