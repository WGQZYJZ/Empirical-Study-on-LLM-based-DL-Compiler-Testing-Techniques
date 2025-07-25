import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(64, 3, 3, stride=1)
        self.conv2 = torch.nn.Conv2d(3, 4, 3)
        self.conv3 = torch.nn.Conv2d(4, 4, 1, stride=2)
        self.conv4 = torch.nn.Conv2d(4, 6, 1)
        self.conv5 = torch.nn.Conv2d(6, 10, 1)
        self.conv6 = torch.nn.Conv2d(10, 32, 1)
        self.conv7 = torch.nn.Conv2d(32, 20, 3, stride=2)
        self.conv8 = torch.nn.Conv2d(20, 20, 1)
        self.conv9 = torch.nn.Conv2d(20, 12, 1)
        self.conv10 = torch.nn.Conv2d(12, 20, 1)
        self.conv11 = torch.nn.Conv2d(20, 10, 1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        v8 = torch.relu(v7)
        v9 = self.conv5(v8)
        v10 = torch.relu(v9)
        v11 = self.conv6(v10)
        v12 = torch.relu(v11)
        v0 = torch.nn.functional.max_pool2d(v12, kernel_size=[3, 3], stride=1, padding=0, ceil_mode=False)
        v13 = self.conv7(v0)
        v14 = torch.relu(v13)
        v15 = self.conv8(v14)
        v16 = torch.relu(v15)
        v17 = self.conv9(v16)
        v18 = torch.relu(v17)
        v19 = self.conv10(v18)
        v20 = torch.relu(v19)
        v21 = self.conv11(v20)
        v22 = torch.nn.functional.max_unpool2d(v21, v22, kernel_size=[3, 3], stride=1, padding=0, output_size=None, ceil_mode=False)
        v23 = torch.relu(v22)
        return v23
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64, 28, 28)
x1.shape
v22 = torch.randn(1, 64, 16, 16)
v22.shape
