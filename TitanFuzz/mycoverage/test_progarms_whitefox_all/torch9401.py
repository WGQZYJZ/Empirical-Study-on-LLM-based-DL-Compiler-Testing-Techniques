import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, (1, 1), stride=7, padding=0)
        self.conv2 = torch.nn.Conv2d(64, 21, (1, 1), stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(21, 64, (1, 1), stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(64, 69, (1, 1), stride=2, padding=0)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = torch.sigmoid(v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 512, 256)
