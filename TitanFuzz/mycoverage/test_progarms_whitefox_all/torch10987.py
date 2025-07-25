import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 3, stride=1, padding=0, dilation=1)
        self.conv2 = torch.nn.Conv2d(6, 12, 3, stride=1, padding=1, dilation=1)
        self.conv3 = torch.nn.Conv2d(12, 24, 3, stride=1, padding=0, dilation=2)
        self.conv4 = torch.nn.Conv2d(24, 48, 3, stride=1, padding=1, dilation=1)
        self.conv5 = torch.nn.Conv2d(48, 96, 3, stride=1, padding=0, dilation=4)
        self.conv6 = torch.nn.Conv2d(96, 192, 3, stride=1, padding=1, dilation=1)
        self.conv7 = torch.nn.Conv2d(192, 384, 3, stride=1, padding=0, dilation=8)
        self.conv8 = torch.nn.Conv2d(384, 768, 3, stride=1, padding=2, dilation=1)
        self.conv9 = torch.nn.Conv2d(768, 1024, 3, stride=1, padding=0, dilation=16)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv3(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.conv4(v6)
        v8 = torch.sigmoid(v7)
        v9 = self.conv5(v8)
        v10 = torch.sigmoid(v9)
        v11 = self.conv6(v10)
        v12 = torch.sigmoid(v11)
        v13 = self.conv7(v12)
        v14 = torch.sigmoid(v13)
        v15 = self.conv8(v14)
        v16 = torch.sigmoid(v15)
        v17 = self.conv9(v16)
        v18 = torch.sigmoid(v17)
        return v18
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 112, 112)
