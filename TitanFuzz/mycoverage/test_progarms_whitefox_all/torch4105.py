import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(768, 768, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(768, 1024, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.tanh(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 768, 8, 8)
