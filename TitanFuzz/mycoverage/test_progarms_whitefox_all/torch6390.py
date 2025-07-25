import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 32, 3, padding=1)
        self.conv1 = torch.nn.ConvTranspose2d(32, 16, 3, padding=1)
        self.conv2 = torch.nn.ConvTranspose2d(16, 8, 3, padding=1)
        self.conv3 = torch.nn.ConvTranspose2d(8, 3, 3, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv1(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv2(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.conv3(v6)
        v8 = torch.sigmoid(v7)
        return v8
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 32, 32)
