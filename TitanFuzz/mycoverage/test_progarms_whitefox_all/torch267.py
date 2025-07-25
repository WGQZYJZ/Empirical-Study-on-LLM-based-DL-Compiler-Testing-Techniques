import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(2, 8, 3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1.unsqueeze(1))
        v2 = self.conv2(x1.unsqueeze(1))
        v2 = v2 - 0.5
        v3 = F.relu(v1 - v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
