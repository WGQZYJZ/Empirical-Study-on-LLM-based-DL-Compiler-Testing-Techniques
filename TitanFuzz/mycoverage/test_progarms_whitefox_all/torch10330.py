import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, padding=1, stride=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 7, padding=3, stride=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 3, padding=1, stride=1)
        self.conv4 = torch.nn.Conv2d(3, 8, 5, padding=2, stride=1)
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.conv3(x3)
        v4 = self.conv4(x4)
        v5 = torch.cat((v1,v2),1) + v3 + v4
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 196, 196)
x2 = torch.randn(1, 3, 196, 196)
x3 = torch.randn(1, 3, 196, 196)
x4 = torch.randn(1, 3, 196, 196)
