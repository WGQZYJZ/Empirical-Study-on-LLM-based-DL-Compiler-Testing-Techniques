import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 4, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 0.5
        v3 = F.relu(v2)
        v4 = self.conv2(v3)
        v5 = v4 - 0.6
        v6 = F.relu(v5)
        v7 = v6.view(v6.size(0), -1)
        v8 = torch.mean(v7, 1)
        return v8
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
