import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, 1, stride=1, padding=0)
        self.bn1 = nn.BatchNorm2d(32)
        self.up = nn.Upsample(size=(480,270), mode='bilinear')
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.bn1(v1)
        v3 = torch.sigmoid(v2)
        v4 = self.up(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 480, 270)
