import torch
from torch import nn

class ModelTanh(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 32, 1, stride=(2, 2))
        self.conv2 = torch.nn.Conv2d(32, 64, 1, stride=(2, 2))
        self.conv3 = torch.nn.Conv2d(64, 64, 1)
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.tanh(v1)
        v3 = self.conv2(v2)
        v4 = torch.tanh(v3)
        v5 = self.conv3(v4)
        return v5
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 64, 64)
