import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(6, 20, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(20, 40, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(40, 60, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(60, 80, 3, stride=1, padding=1)
    def forward(self, x1):
        v1 = torch.nn.functional.pad(x1, (2, 2, 0, 0), 'constant', 0)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = self.conv3(v3)
        v5 = self.conv4(v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 512, 512)
