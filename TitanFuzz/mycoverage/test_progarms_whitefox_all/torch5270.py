import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(8, 8, 5, stride=2, padding=3)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 0.25
        v3 = F.relu(v2)
        return self.conv2(v3)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 48, 48)
