import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(6, 64, 3, stride=1, padding=0)
        self.conv1 = torch.nn.ConvTranspose2d(64, 3, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 256, 256)
