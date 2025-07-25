import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=3, padding=2)
        self.conv2 = torch.nn.Conv2d(8, 16, 2, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 32, 2, stride=2, padding=2)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 14
        v3 = F.relu(v2)
        v4 = self.conv2(v3)
        v5 = v4 - 2
        v6 = F.relu(v5)
        v7 = self.conv3(v6)
        v8 = v7 - 32
        v9 = F.relu(v8)
        return v9
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 112, 112)
