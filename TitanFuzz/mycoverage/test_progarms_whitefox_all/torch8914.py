import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(128, 32, (3, 3), stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 16, (3, 3), stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 4, (1, 3), stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(32, 8, (3, 3), stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(8, 2, (1, 3), stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v1)
        v5 = self.conv5(v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 128, 16, 7)
