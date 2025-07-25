import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 32, 3, padding=1, stride=1)
        self.conv2 = torch.nn.ConvTranspose2d(32, 64, 3, padding=1, stride=2)
        self.conv3 = torch.nn.ConvTranspose2d(64, 128, 3, padding=1, stride=1)
        self.conv4 = torch.nn.ConvTranspose2d(128, 9, 3, padding=1, stride=2)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(8, 3, 16, 16)
