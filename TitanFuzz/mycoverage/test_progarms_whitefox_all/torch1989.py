import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, 3, padding=1, bias=False)
        self.bn = torch.nn.BatchNorm2d(6, track_running_stats=True)
    def forward(self, x):
        return self.bn(self.conv(x))
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 4, 4)
