import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 16, (3, 5), stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(16, 16, (3, 5), stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(16, 16, (3, 5), stride=2, padding=0)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv3(v4)
        v6 = torch.sigmoid(v5)
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
