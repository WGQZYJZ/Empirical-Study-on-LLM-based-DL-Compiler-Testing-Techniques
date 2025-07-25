import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - torch.randn((3, 36, 36))
        v3 = F.relu(v2)
        v4 = self.conv3(v3)
        v5 = v4 - torch.randn((3, 36, 36))
        v6 = F.relu(v5)
        v7 = self.conv2(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
