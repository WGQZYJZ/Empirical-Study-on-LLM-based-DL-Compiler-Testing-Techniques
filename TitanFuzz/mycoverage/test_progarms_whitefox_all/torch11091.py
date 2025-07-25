import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v1 + x
        v4 = torch.relu(v3)
        v5 = self.conv3(v2)
        v6 = v5 + x
        v7 = torch.relu(v6)
        return v7
m = Model()
# INPUTS TO THE MODEL
x = torch.randn(1, 16, 64, 64)
# MODEL END