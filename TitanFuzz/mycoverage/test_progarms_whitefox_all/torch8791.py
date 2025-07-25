import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), bias=False)
        self.conv2 = torch.nn.Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), bias=False)
        self.conv3 = torch.nn.Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), bias=False)
        self.conv4 = torch.nn.Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), bias=False)
        self.conv5 = torch.nn.Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), bias=False)
        self.conv6 = torch.nn.Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), bias=False)
    def forward(self, x1):
        v1 = self.conv3(self.conv1(x1))
        v2 = self.conv5(self.conv2(v1))
        v3 = self.conv6(torch.sigmoid(self.conv4(v2)))
        v4 = F.relu(v3)
        return v4
m = Model()
# Inputs to the model
x2 = torch.randn(1, 3, 32, 32)
