import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(20, 10, kernel_size=(1, 1), stride=1, padding=0, bias=True)
        self.conv2 = torch.nn.Conv2d(10, 22, kernel_size=(3, 3), stride=1, padding=1, bias=False)
        self.conv3 = torch.nn.Conv2d(22, 12, kernel_size=(1, 1), stride=1, padding=0, bias=True)
        self.conv4 = torch.nn.Conv2d(12, 22, kernel_size=(3, 3), stride=1, padding=1, bias=False)
        self.conv5 = torch.nn.Conv2d(22, 384, kernel_size=(1, 1), stride=1, padding=0, bias=True)
        self.conv6 = torch.nn.Conv2d(384, 1, kernel_size=(1, 1), stride=1, padding=0, bias=True)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = self.conv6(v5)
        v7 = v6
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(1, 20, 224, 224)
