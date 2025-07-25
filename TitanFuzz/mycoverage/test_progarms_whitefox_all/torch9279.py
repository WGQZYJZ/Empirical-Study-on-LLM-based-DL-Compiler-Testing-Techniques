import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 10, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(10, 10, 5, stride=1, padding=2)
        self.conv3 = torch.nn.Conv2d(10, 10, 7, stride=3, padding=3)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = torch.sigmoid(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
