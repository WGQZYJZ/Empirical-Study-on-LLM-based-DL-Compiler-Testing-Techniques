import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.maxpool1 = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(num_features = 5)
        self.maxpool2 = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(num_features = 4)
        self.conv1 = torch.nn.Conv2d(in_channels=4, out_channels=4, kernel_size=1, stride=1)
        self.conv2 = torch.nn.Conv2d(in_channels=4, out_channels=4, kernel_size=1, stride=1)
        self.conv3 = torch.nn.Conv2d(in_channels=8, out_channels=4, kernel_size=1, stride=1)
        self.conv4 = torch.nn.Conv2d(in_channels=8, out_channels=4, kernel_size=1, stride=1)
    def forward(self, x1):
        v1 = self.maxpool1(x1)
        v2 = self.bn1(v1)
        v3 = self.maxpool2(x1)
        v4 = self.bn2(v3)
        v5 = torch.cat((v2, v4), 1)
        v6 = self.conv1(v5)
        v7 = torch.sigmoid(v6)
        v8 = self.bn1(v7)
        v9=torch.cat((v7,v8),1)
        v10=self.conv2(v9)
        v11 = torch.softmax(v10)
        v12 = self.maxpool1(x1)
        v13 = self.bn2(v12)
        v14 = torch.cat((v11, v13), 1)
        v15 = self.conv3(v14)
        v16 = torch.sigmoid(v15)
        v17 = self.maxpool2(x1)
        v18 = self.bn1(v17)
        v19 = torch.cat((v16, v18), 1)
        v20 = self.conv4(v19)
        v21 = torch.sigmoid(v20)
        return v21
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
