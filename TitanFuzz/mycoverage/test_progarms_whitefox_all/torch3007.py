import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(5, 32, 1)
        self.conv2 = torch.nn.Conv2d(32, 5, 1)
        self.conv3 = torch.nn.Conv2d(5, 32, 1)
        self.conv4 = torch.nn.Conv2d(32, 5, 1)
        self.conv5 = torch.nn.Conv2d(5, 16, 1)
        self.conv6 = torch.nn.Conv2d(16, 4, 1)
        self.conv7 = torch.nn.Conv2d(4, 32, 1)
        self.conv8 = torch.nn.Conv2d(32, 10, 1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = torch.mul(v4, 1.0)
        v6 = self.conv3(v5)
        v7 = torch.sigmoid(v6)
        v8 = self.conv4(v7)
        v9 = torch.sigmoid(v8)
        v10 = torch.mul(v9, 1.0)
        v11 = self.conv5(v10)
        v12 = torch.sigmoid(v11)
        v13 = self.conv6(v12)
        v14 = torch.sigmoid(v13)
        v15 = torch.mul(v14, 1.0)
        v16 = self.conv7(v15)
        v17 = torch.sigmoid(v16)
        v18 = self.conv8(v17)
        v19 = torch.sigmoid(v18)
        return v19
m = Model()
# Inputs to the model
x1 = torch.randn(1, 5, 244, 244)
