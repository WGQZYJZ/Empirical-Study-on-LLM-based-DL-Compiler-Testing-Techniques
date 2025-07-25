import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 128, 3, stride=2, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(128, 32, 4, stride=2, padding=1)
        self.conv = torch.nn.ConvTranspose2d(32, 8, 1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv_transpose(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv(v4)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3, 222, 222)
# Model starts