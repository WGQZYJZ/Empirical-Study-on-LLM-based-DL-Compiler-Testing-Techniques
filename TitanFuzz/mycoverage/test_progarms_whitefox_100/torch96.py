import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(6, 5, 3, bias=False, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(6, 5, 3, bias=False, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(v2)
        v4 = v3 + 1
        v5 = self.conv3(v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 128, 60)
