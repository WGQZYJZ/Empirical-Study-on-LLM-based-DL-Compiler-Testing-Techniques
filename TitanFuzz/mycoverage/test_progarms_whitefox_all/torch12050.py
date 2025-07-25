import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(3, 1, 3, stride=1, dilation=1, padding=1)
        self.conv_2 = torch.nn.Conv2d(2, 2, 1, stride=1, dilation=1, padding=0)
    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = self.conv_2(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
