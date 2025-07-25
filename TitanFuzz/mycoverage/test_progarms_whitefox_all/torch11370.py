import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.conv2 = torch.nn.Conv2d(16, 64, kernel_size=(1, 1), stride=(2, 2), groups=2)
        self.bn = torch.nn.BatchNorm2d(64)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v2 - 1
        v4 = F.relu(v3)
        v5 = self.bn(v4)
        v6 = v5 - 3
        v7 = F.relu(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
