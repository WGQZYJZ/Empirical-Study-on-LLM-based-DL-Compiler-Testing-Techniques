import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(6, 7, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(7, 8, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv3(v4)
        v6 = torch.tanh(v5)
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3, 32, 32)
