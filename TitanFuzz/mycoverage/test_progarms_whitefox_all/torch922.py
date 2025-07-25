import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
    def forward(self, x1, x2):
        v1 = x1 + x2
        v2 = self.conv1(v1)
        v3 = torch.sigmoid(v2)
        v4 = v2 * v3
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 32, 224, 28)
x2 = torch.randn(1, 32, 224, 28)
