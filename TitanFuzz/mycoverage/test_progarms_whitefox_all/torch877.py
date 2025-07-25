import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=2, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v2 - 0.5
        v4 = F.relu(v3)
        v5 = torch.squeeze(v4, 0)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
