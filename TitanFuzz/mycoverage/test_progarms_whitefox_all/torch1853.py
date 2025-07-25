import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 5, 5, stride=2, padding=2)
        self.avg = torch.nn.AvgPool2d(kernel_size=2, stride=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 0.98
        v3 = self.avg(v2)
        v4 = F.relu(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
