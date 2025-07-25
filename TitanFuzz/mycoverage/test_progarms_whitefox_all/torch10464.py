import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, (5, 5), stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, (5, 5), stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 3, (3, 3), stride=2, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = torch.sigmoid(v1)
        v5 = torch.sigmoid(v2)
        v6 = torch.sigmoid(v3)
        v7 = v1 * v4
        t8 = v2 * v5
        t9 = v3 * v6
        t10 = torch.tanh(t8)
        t11 = torch.tanh(t9)
        v12 = v7 + t10
        t13 = v12 + t11
        v14 = torch.tanh(t13)
        return v14
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
